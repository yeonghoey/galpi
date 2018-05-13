#!/usr/bin/env bash

set -euo pipefail

readonly STAGE="${1:-prod}"
readonly REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
readonly APP_DIR="${REPO_DIR}/app"

cd "${APP_DIR}"

# Build
#############################################################
npm run build
# Ensure the build result actually exists
[[ -d "${APP_DIR}/dist" ]]
[[ -f "${APP_DIR}/dist/index.html" ]]

# Deploy
#############################################################
param() {
  local name
  name="/galpi/${STAGE}/$1"
  pipenv run aws ssm get-parameter \
         --name "${name}" \
         --query 'Parameter.Value' \
         --output text
}

readonly BUCKET="$(param bucket)"
readonly DISTRIBUTION_ID="$(param distribution_id)"

# Upload the build result to S3
pipenv run aws s3 sync "${APP_DIR}/dist" "s3://${BUCKET}" \
       --exact-timestamps \
       --delete

# Invalidate CloudFront
pipenv run aws cloudfront create-invalidation \
       --distribution-id "${DISTRIBUTION_ID}" \
       --paths '/*'
