# AWS Lambda and S3 Integration Tutorial

## Introduction
This repository provides a comprehensive guide and scripts for integrating AWS Lambda with S3.
It includes detailed instructions for setting up IAM roles, S3 buckets, deploying Lambda functions, and testing the integration thoroughly.

## Repository Contents
- `Instructions part 1 IAM role, S3, Lambda function.pdf`: Step-by-step guide for setting up IAM roles, S3 buckets, and Lambda functions.
- `Instructions part 2 Testing and test result.pdf`: Instructions for testing the Lambda function and documentation of expected results.
- `lambda_function.zip`: A zipped Lambda function package ready for deployment.

Inside the `scripts` folder:
- `create_files.py`: A Python script to generate test files.
- `upload_s3_files_to_bucket.py`: A Python script using threading for optimized file uploading to S3, with logging functionality.

## Getting Started
1. **IAM Role and S3 Bucket**: Consult `Instructions part 1 IAM role, S3, Lambda function.pdf` for initial setup.
2. **Lambda Function**: Deploy your Lambda function using the provided `lambda_function.zip`.
3. **Testing**: Follow the `Instructions part 2 Testing and test result.pdf` to ensure everything is working correctly.

## Script Usage
- `create_files.py` is designed to create dummy files for testing.
- `upload_s3_files_to_bucket.py` utilizes threading to enhance the upload process to S3, including logging for monitoring the upload process.

## Author
Created by Lior Kovtun. All materials in this repository are created by me and reflect my knowledge and skills in AWS services.

