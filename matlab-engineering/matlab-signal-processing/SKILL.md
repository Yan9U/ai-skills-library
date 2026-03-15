---
name: matlab-signal-processing
description: Use when implementing MATLAB signal-processing workflows such as filtering, FFT, PSD, denoising, resampling, peak detection, feature extraction, or time-frequency analysis.
---

# MATLAB Signal Processing

## Purpose

Build stable signal-processing pipelines in MATLAB with explicit sampling assumptions and validated outputs.

## When to use

- FFT and spectrum analysis
- Filtering and denoising
- PSD and spectrogram workflows
- Resampling and interpolation
- Peak detection and feature extraction

Read [../references/matlab-mcp-guardrails.md](../references/matlab-mcp-guardrails.md) before using toolbox-dependent APIs.

## Workflow

1. Define sample rate, units, time base, and signal orientation.
2. Choose the minimal correct transform or filter.
3. State edge handling, windowing, and normalization choices.
4. Validate outputs against a known baseline or synthetic case.
5. Export figures and metrics with units.

## Always

- State `Fs` explicitly.
- Check whether the signal is row- or column-oriented.
- Avoid phase distortion unless it is acceptable.
- Separate preprocessing from analysis.
- Confirm whether Signal Processing Toolbox functions are required.

## Example code

```matlab
Fs = 1000;
[pxx, f] = pwelch(x, [], [], [], Fs);
plot(f, 10*log10(pxx)); grid on
xlabel('Frequency (Hz)'); ylabel('PSD (dB/Hz)');
```
