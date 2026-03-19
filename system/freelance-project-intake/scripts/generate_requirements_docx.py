#!/usr/bin/env python3

"""Generate a simple client questionnaire DOCX from a JSON file."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape
import zipfile


CONTENT_TYPES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
"""


ROOT_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""


APP_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
            xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>AI Skill Helper</Application>
</Properties>
"""


LABELS = {
    "zh-CN": {
        "document_title": "客户需求确认问卷",
        "client": "客户",
        "prepared_for": "提交对象",
        "prepared_by": "编制人",
        "document_date": "文档日期",
        "project_summary": "项目概述",
        "known_constraints": "已知约束",
        "next_steps": "后续步骤",
        "unknown_client": "未提供客户名称",
        "not_specified": "未说明",
    },
    "en": {
        "document_title": "Client Requirements Questionnaire",
        "client": "Client",
        "prepared_for": "Prepared for",
        "prepared_by": "Prepared by",
        "document_date": "Document date",
        "project_summary": "Project Summary",
        "known_constraints": "Known Constraints",
        "next_steps": "Next Steps",
        "unknown_client": "Unknown client",
        "not_specified": "Not specified",
    },
}


def build_core_xml(title: str) -> str:
    created = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
                   xmlns:dc="http://purl.org/dc/elements/1.1/"
                   xmlns:dcterms="http://purl.org/dc/terms/"
                   xmlns:dcmitype="http://purl.org/dc/dcmitype/"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>{escape(title)}</dc:title>
  <dc:creator>AI Skill Helper</dc:creator>
  <cp:lastModifiedBy>AI Skill Helper</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{created}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{created}</dcterms:modified>
</cp:coreProperties>
"""


def paragraph_xml(text: str, *, bold: bool = False, center: bool = False) -> str:
    text = escape(text)
    run_props = "<w:rPr><w:b/></w:rPr>" if bold else ""
    para_props = '<w:pPr><w:jc w:val="center"/></w:pPr>' if center else ""
    return (
        "<w:p>"
        f"{para_props}"
        "<w:r>"
        f"{run_props}"
        f'<w:t xml:space="preserve">{text}</w:t>'
        "</w:r>"
        "</w:p>"
    )


def blank_paragraph_xml() -> str:
    return "<w:p/>"


def build_document_xml(payload: dict, language: str) -> str:
    labels = LABELS[language]
    title = payload["project_title"]
    client_name = payload.get("client_name", labels["unknown_client"])
    prepared_for = payload.get("prepared_for", labels["not_specified"])
    prepared_by = payload.get("prepared_by", labels["not_specified"])
    document_date = payload.get("document_date", labels["not_specified"])
    summary = payload.get("project_summary", [])
    constraints = payload.get("known_constraints", [])
    sections = payload.get("question_sections", [])
    next_steps = payload.get("next_steps", [])

    body_parts = [
        paragraph_xml(labels["document_title"], bold=True, center=True),
        paragraph_xml(title, bold=True, center=True),
        blank_paragraph_xml(),
        paragraph_xml(f'{labels["client"]}: {client_name}', bold=True),
        paragraph_xml(f'{labels["prepared_for"]}: {prepared_for}'),
        paragraph_xml(f'{labels["prepared_by"]}: {prepared_by}'),
        paragraph_xml(f'{labels["document_date"]}: {document_date}'),
        blank_paragraph_xml(),
        paragraph_xml(labels["project_summary"], bold=True),
    ]

    for item in summary:
        body_parts.append(paragraph_xml(f"- {item}"))

    if constraints:
        body_parts.append(blank_paragraph_xml())
        body_parts.append(paragraph_xml(labels["known_constraints"], bold=True))
        for item in constraints:
            body_parts.append(paragraph_xml(f"- {item}"))

    question_number = 1
    for section in sections:
        body_parts.append(blank_paragraph_xml())
        body_parts.append(paragraph_xml(section["title"], bold=True))
        purpose = section.get("purpose")
        if purpose:
            body_parts.append(paragraph_xml(purpose))
        for question in section.get("questions", []):
            body_parts.append(paragraph_xml(f"{question_number}. {question}"))
            question_number += 1

    if next_steps:
        body_parts.append(blank_paragraph_xml())
        body_parts.append(paragraph_xml(labels["next_steps"], bold=True))
        for item in next_steps:
            body_parts.append(paragraph_xml(f"- {item}"))

    body_parts.append(
        "<w:sectPr>"
        '<w:pgSz w:w="12240" w:h="15840"/>'
        '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
        'w:header="720" w:footer="720" w:gutter="0"/>'
        "</w:sectPr>"
    )

    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body>"
        + "".join(body_parts)
        + "</w:body></w:document>"
    )


def load_payload(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    required_fields = ["project_title", "question_sections"]
    missing = [field for field in required_fields if field not in payload]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    return payload


def write_docx(payload: dict, output_path: Path, language: str) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    title = payload["project_title"]
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", CONTENT_TYPES_XML)
        docx.writestr("_rels/.rels", ROOT_RELS_XML)
        docx.writestr("docProps/app.xml", APP_XML)
        docx.writestr("docProps/core.xml", build_core_xml(title))
        docx.writestr("word/document.xml", build_document_xml(payload, language))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to the questionnaire JSON file")
    parser.add_argument("--output", required=True, help="Path to the output DOCX file")
    parser.add_argument(
        "--language",
        default="zh-CN",
        choices=sorted(LABELS),
        help="Output language for generated labels and headings",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    payload = load_payload(input_path)
    write_docx(payload, output_path, args.language)
    print(f"Wrote questionnaire DOCX to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
