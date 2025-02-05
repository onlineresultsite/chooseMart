# name: Build & Deploy Django

# on:
#   push:
#     branches:
#       - main

# env:
#   CI: false

# jobs:
#   build:
#     name: Build
#     runs-on: ubuntu-latest

#     steps:
#       - name: Checkout repo
#         uses: actions/checkout@v2

#       - name: Set up Python
#         uses: actions/setup-python@v4
#         with:
#           python-version: '3.8'

#       - name: Install dependencies
#         run: |
#           python -m venv venv
#           . venv/bin/activate
#           pip install -r requirements.txt

#       - name: Run tests
#         run: |
#           . venv/bin/activate
#           python manage.py test

#       - name: Collect static files
#         run: |
#           . venv/bin/activate
#           python manage.py collectstatic --noinput

#       - name: List static directory
#         run: ls -la static

#       - name: Upload static files
#         uses: actions/upload-artifact@v4
#         with:
#           name: static-files
#           path: static/

#   deploy:
#     name: Deploy
#     needs: build
#     runs-on: ubuntu-latest
#     if: github.ref == 'refs/heads/main'

#     steps:
#       - name: Decode and save SSH key
#         run: |
#           echo "${{ secrets.EC2_SSH_KEY }}" | base64 -d > /tmp/chooseMart.pem
#           chmod 600 /tmp/chooseMart.pem

#       - name: List /tmp directory
#         run: ls -la /tmp

#       - name: Download static files
#         uses: actions/download-artifact@v4
#         with:
#           name: static-files
#           path: static/

#       - name: List static directory
#         run: ls -la static

#       # - name: Sync static files to S3
#       #   run: |
#       #     aws s3 sync static/ s3://choosemart/static/
#       #   env:
#       #     AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
#       #     AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
#       #     AWS_REGION: ${{ secrets.AWS_REGION }}

#       - name: Deploy to EC2
#         run: |
#           scp -o StrictHostKeyChecking=no -i /tmp/chooseMart.pem -r . ${{ secrets.EC2_HOST }}:/home/ubuntu/myproject
#           ssh -o StrictHostKeyChecking=no -i /tmp/chooseMart.pem ${{ secrets.EC2_HOST }} 'cd /home/ubuntu/myproject && docker-compose down && docker-compose up -d'
#         env:
#           CI: false
#           AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
#           AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
#           AWS_REGION: ${{ secrets.AWS_REGION }}
