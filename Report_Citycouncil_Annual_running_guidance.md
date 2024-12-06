# City Council Annual Redaction

## Overview

This guidance outlines the steps to configure, execute, and verify the functionality of the `Redaction_Annual.py` script, designed to redact sensitive data in annual reports based on specified rules and configurations.

## Prerequisites

1. **Python Installation** :

* Ensure Python 3.8 or higher is installed on your system.
* Install required libraries: `pip install openpyxl`

1. **File Organization** :

* **Input Files** : Saved in: `R:\SEO Analytics\Reporting\City Council\City Council SY24\Annual Reports\Non-Redacted Annual Special Education Data Report SY24.xlsx`
* **Output Files** :

  * **Unredacted Copies** : Saved in: `C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CityCouncil\CCUnredacted`

    **Redacted Copies** : Saved in: `C:\Users\Ywang36\OneDrive - NYCDOE\Desktop` and rename it from `Non-Redacted Annual Special Education Data Report SY24.xlsx` to `Redacted Annual Special Education Data Report SY24.xlsx` after running `Redaction_Annual.py` and mannualy copy it to `R:\SEO Analytics\Reporting\City Council\City Council SY24\Annual Reports\Redacted Annual Special Education Data Report SY24.xlsx` after QC it

1. **Configuration Files** :

* Ensure the required configuration files (`redaction_config.py`, `redaction_config_SY23.py`, `redaction_config_SY24.py`) are in the same directory as `Redaction_Annual.py`.

1. **File Naming Convention** :

* Ensure files adhere to the naming conventions: `Non-Redacted Annual Special Education Data Report SYXX.xlsx`

  Replace `SYXX` with the school year (e.g., SY21, SY22).

## Key Parameters to Adjust

* **School Years to Process** :
  Modify the list in `processor.copy_reports()` to include the desired school years: `processor.copy_reports(['SY21', 'SY22', 'SY23', 'SY24'])`
* **File Configurations** :
  Update the `file_configs` list with filenames and corresponding configuration objects: `file_configs = [('C:`

## Advanced Usage

1. **Add New School Year** :

* Create a new configuration file (e.g., `redaction_config_SY25.py`).
* Add it to the `file_configs` list.

1. **Test Specific Reports** :

* Modify `file_configs` to include only the desired report and configuration.

1. If SY25 has same format as SY24, don't need to create `redaction_config_SY25.py`, just use `redaction_config_SY24.py`

## Some Overredactions need to be manually done accordind to limitations

1.same value but since Python always redacts from left to right so it picks the left one but actually the right one is optimal

https://seoanalytics.atlassian.net/browse/MIS-12161?atlOrigin=eyJpIjoiMDk1NzlmNTQxMTllNDQ5OWI5N2ZlNWEyNjZlNjY0NDUiLCJwIjoiaiJ9

Explanation: This one has to be manually fixed because there are two 0 and Python will always redact the first 0 it finds

2.initial masking masked the smallest unredacted data in the same column when <5 accured but futhur masking masked other data

https://seoanalytics.atlassian.net/browse/MIS-12159?atlOrigin=eyJpIjoiYTVmZTgwYmJjYzI0NDU5Njk1NTgzNWRhYWZkMDVmMzIiLCJwIjoiaiJ9
