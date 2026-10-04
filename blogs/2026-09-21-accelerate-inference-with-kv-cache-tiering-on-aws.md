---
title: "Accelerate inference with KV cache tiering on AWS"
url: "https://aws.amazon.com/blogs/storage/accelerate-inference-with-kv-cache-tiering-on-aws/"
date: "2026-09-21"
author: "Siva Devabakthini"
feed_url: "https://aws.amazon.com/blogs/storage/feed/"
---
When running large language model (LLM) inference at scale on AWS, the GPU might not be the only thing that limits you. The GPU generates tokens fast, but what then contributes to performance is everything around it: memory, storage, and the network path that connects them. That’s the difference between a demo and production.
