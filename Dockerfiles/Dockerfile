FROM docker.repository.cloudera.com/cloudera/cdsw/ml-runtime-pbj-workbench-python3.10-standard:2025.01.1-b8
# Install tesseract in the new image
RUN apt-get update && apt-get upgrade -y && apt-get install -y tesseract-ocr poppler-utils && apt-get clean && rm -rf /var/lib/apt/lists/*
# Install the python wrapper pytesseract and pillow
RUN pip install --no-cache-dir pytesseract pillow pdf2image
# Override Runtime label and environment variables metadata
ENV ML_RUNTIME_EDITION="Tesseract Edition" \
       	ML_RUNTIME_SHORT_VERSION="1.2" \
        ML_RUNTIME_MAINTENANCE_VERSION=1 \
        ML_RUNTIME_DESCRIPTION="Tesseract Engine"
ENV ML_RUNTIME_FULL_VERSION="${ML_RUNTIME_SHORT_VERSION}.${ML_RUNTIME_MAINTENANCE_VERSION}"
LABEL com.cloudera.ml.runtime.edition=$ML_RUNTIME_EDITION \
        com.cloudera.ml.runtime.full-version=$ML_RUNTIME_FULL_VERSION \
        com.cloudera.ml.runtime.short-version=$ML_RUNTIME_SHORT_VERSION \
        com.cloudera.ml.runtime.maintenance-version=$ML_RUNTIME_MAINTENANCE_VERSION \
        com.cloudera.ml.runtime.description=$ML_RUNTIME_DESCRIPTION
