# fml-slack-bot

https://www.fmylife.com/ の投稿をランダムにslackのチャンネルにポストするbot

機械翻訳付き

## Architecture
![architecture](architecture.drawio)

## How to deploy

このリポジトリの `master` ブランチを更新するとCodepipelineが走る


## 使用技術

- 実行
  - AWS Lambda
    - Python3.7
  - Amazon Translate
- CI/CD
  - GitHub
  - CodePipeline
  - CodeBuild
  - CloudFormation
