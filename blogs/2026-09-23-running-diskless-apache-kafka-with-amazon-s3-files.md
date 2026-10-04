---
title: "Running diskless Apache Kafka with Amazon S3 Files"
url: "https://aws.amazon.com/blogs/storage/running-diskless-apache-kafka-with-amazon-s3-files/"
date: "2026-09-23"
author: "Akshaya Shah"
feed_url: "https://aws.amazon.com/blogs/storage/feed/"
---
Apache Kafka usually stores its logs on local disk, which fills up and forces teams to offload data and maintain custom tooling. With Amazon S3 Files, you can mount an S3 bucket as an NFS file system and point Kafka's log directories to it, running diskless Kafka. This post shows how, with a multi-Region setup and performance benchmarks.
