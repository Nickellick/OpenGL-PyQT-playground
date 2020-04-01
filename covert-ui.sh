#!/bin/bash
# This version does not support subfolders (not recursive)
# WARNING! All filenames will be capitalized and a "UI" will be added at the end

# Specify ui files location and destination folder of the QT ui files
QT_UI_FOLDER="./ui"
PYTHON_UI_FOLDER="./PythonUI"

QT_UI_FILES="${QT_UI_FOLDER}/*"

for UI_FILE in ${QT_UI_FILES}
do
  UI_FILE_BASENAME=$(basename ${UI_FILE} | sed 's/[^ _-]*/\u&/g')
  pyuic5 "${UI_FILE}" -o "${PYTHON_UI_FOLDER}"/"${UI_FILE_BASENAME%.*}"UI.py
done