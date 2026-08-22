# Amazon S3 (amazon-s3)

<!-- API-EVANGELIST-PROVENANCE:BEGIN -->
> ### About this repository
>
> **This is not our API.** This repository is an independent, third-party profile of a company's
> **publicly available** API surface, maintained by [API Evangelist](https://apievangelist.com).
> API Evangelist does not operate, host, resell, or support this company's APIs, and is not
> affiliated with or endorsed by the company unless stated on the profile.
>
> **Where the information came from.** Everything here is assembled from material a member of the
> public can reach with a browser and no credentials — the company's own website, developer portal
> and documentation, the specifications it publishes for public use (OpenAPI, AsyncAPI, JSON Schema,
> `apis.json`, `llms.txt` and similar), its public repositories, and its public status, pricing and
> changelog pages. **Nothing here is obtained by breaching a system, defeating an access control, or
> using credentials of any kind.**
>
> **The rating is an independent assessment.** The Kin Score and Agent Readiness rating are
> independently calculated scores of a company's *public* API artifacts, produced by API Evangelist
> against a published rubric. They are not certifications, endorsements, security assessments, or
> audits, and they score published artifacts — not the quality, safety, or security of the software.
>
> **Corrections, re-scores, and removal are free.** No partnership, contract, or purchase is
> required, and you do not need to justify the request.
>
> - **Something wrong?** Open an issue on this repository, or email
>   [info@apievangelist.com](mailto:info@apievangelist.com).
> - **Published something new?** Ask for a re-score and we will re-run the rating.
> - **Want the listing taken down?** Say so and we will honor it. The profile is reduced to your
>   company name, a factual description, and a link to your own site, and the company is recorded as
>   **unrated** — never scored zero for having asked.
>
> **Response times.** Acknowledgement within **one business day**; removal or restriction within
> **two business days**; corrections and re-scores within **five business days**.
>
> **Not from the company, and here with a question?** You are welcome here — we would rather be the
> front line and point you the right way than have a good report go nowhere. What this repository
> can answer is narrow, though, so it is worth knowing who you are actually looking for:
>
> - **A question about how the API works, an account, billing, or a bug in the service** — that is
>   the company's own support, not us. We profile this API; we do not operate it and cannot see
>   your account.
> - **A bug in an open-source project we only catalog** — file it on that project's own repository.
>   This has happened with a real and correct bug report that reached us instead of the people who
>   could fix it, which helped nobody.
> - **Anything about this listing itself** — the description, the tags, the rating, a missing or
>   wrong artifact — is ours. Open an issue here.
> - **Not sure, or something general about API Evangelist or APIs.io** — open an issue on the
>   [APIs.io Inbox](https://github.com/api-search/inbox) and we will route it.
>
> **This repository contains no software, and we will never ask you to download anything.** There is
> no build, release, installer, or binary here — only text and machine-readable API descriptions, so
> there is nothing here that can be "corrupt" or need "repairing". Any issue, comment, or email
> claiming otherwise and offering a download link is not from us and is hostile. Do not follow the
> link; it is a lure. Report it to GitHub and, if you like, tell us at
> [info@apievangelist.com](mailto:info@apievangelist.com) so we can take it down.
>
> **On a security or compliance team?** Email
> [info@apievangelist.com](mailto:info@apievangelist.com) with *security* in the subject line and
> you will get a person, not a form. We will tell you exactly which public URLs this profile was
> built from so your team can see the same surface we did, and we will take the listing down on
> request while you work through it.
>
> Full detail: **[Where this data comes from](https://apievangelist.com/about/where-our-data-comes-from)**
<!-- API-EVANGELIST-PROVENANCE:END -->

Amazon Simple Storage Service (S3) is an object storage service offering industry-leading scalability, data availability, security, and performance.

**APIs.json:** [https://aws.amazon.com/s3/](https://aws.amazon.com/s3/)

## Tags

- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage

## Timestamps

- **Created:** 2024-01-15
- **Modified:** 2026-05-19

## APIs

### Amazon S3 REST API

RESTful API for Amazon S3 storage operations including bucket management, object operations, and access control.

- **Human URL:** [https://aws.amazon.com/s3/](https://aws.amazon.com/s3/)
- **Base URL:** `https://s3.amazonaws.com`

#### Tags

- AWS
- Cloud Storage
- Object Storage
- Storage

#### Properties

- [Documentation](https://docs.aws.amazon.com/AmazonS3/latest/API/)
- [OpenAPI](openapi/amazon-s3-rest-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/amazon-s3-rest-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/amazon-s3-rest-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [OpenAPI](https://api.apis.guru/v2/specs/amazonaws.com/s3/2006-03-01/openapi.yaml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [JSON Schema](json-schema/amazon-s3-bucket-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/amazon-s3-object-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON-LD](json-ld/amazon-s3-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [Pricing](https://aws.amazon.com/s3/pricing/)
- [Getting Started](https://aws.amazon.com/s3/getting-started/)
- [Authentication](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html)
- [SDK](https://aws.amazon.com/tools/)
- [Status Page](https://status.aws.amazon.com/)
- [Best Practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/best-practices.html)
- [F A Q](https://aws.amazon.com/s3/faqs/)
- [API Reference](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html)
- [Changelog](https://docs.aws.amazon.com/AmazonS3/latest/API/WhatsNew.html)
- [Code Examples](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples.html)
- [Security](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html)

### Amazon S3 Control API

Amazon S3 Control provides API operations for managing S3 account-level settings, access points, Batch Operations jobs, S3 Access Grants, Multi-Region Access Points, and Storage Lens configurations.

- **Human URL:** [https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_AWS_S3_Control.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_AWS_S3_Control.html)
- **Base URL:** `https://s3-control.amazonaws.com`

#### Tags

- Access Control
- AWS
- Batch Operations
- Storage

#### Properties

- [Documentation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_AWS_S3_Control.html)
- [OpenAPI](openapi/amazon-s3-control-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/amazon-s3-control-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/amazon-s3-control-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [OpenAPI](https://api.apis.guru/v2/specs/amazonaws.com/s3control/2018-08-20/openapi.yaml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [JSON-LD](json-ld/amazon-s3-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [Pricing](https://aws.amazon.com/s3/pricing/)
- [Getting Started](https://aws.amazon.com/s3/getting-started/)
- [Authentication](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html)
- [SDK](https://aws.amazon.com/tools/)
- [F A Q](https://aws.amazon.com/s3/faqs/)
- [Changelog](https://docs.aws.amazon.com/AmazonS3/latest/API/WhatsNew.html)

### Amazon S3 Tables API

Amazon S3 Tables API provides operations for managing table buckets and tables stored in Apache Iceberg format, enabling structured tabular data storage in Apache Parquet format within Amazon S3.

- **Human URL:** [https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html)
- **Base URL:** `https://s3tables.amazonaws.com`

#### Tags

- Apache Iceberg
- AWS
- Data Lake
- Storage
- Tables

#### Properties

- [Documentation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html)
- [OpenAPI](openapi/amazon-s3-tables-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/amazon-s3-tables-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/amazon-s3-tables-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON-LD](json-ld/amazon-s3-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [API Reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html)
- [Pricing](https://aws.amazon.com/s3/pricing/)
- [Getting Started](https://aws.amazon.com/s3/getting-started/)
- [Authentication](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html)
- [SDK](https://aws.amazon.com/tools/)
- [F A Q](https://aws.amazon.com/s3/faqs/)

## Common Properties

- [Arazzo Workflows](arazzo/) — [Arazzo Specification](https://spec.openapis.org/arazzo/latest.html)
- [Portal](https://aws.amazon.com/)
- [Documentation](https://docs.aws.amazon.com/s3/)
- [Terms of Service](https://aws.amazon.com/service-terms/)
- [Privacy Policy](https://aws.amazon.com/privacy/)
- [Support](https://aws.amazon.com/premiumsupport/)
- [Blog](https://aws.amazon.com/blogs/storage/)
- [GitHub Organization](https://github.com/aws)
- [Console](https://console.aws.amazon.com/s3/)
- [Sign Up](https://signin.aws.amazon.com/signup?request_type=register)
- [Login](https://aws.amazon.com/console/)
- [Status Page](https://health.aws.amazon.com/health/status)
- [Knowledge Center](https://repost.aws/knowledge-center)
- [YouTube](https://www.youtube.com/user/AmazonWebServices)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/amazon-s3)
- [Contact](https://aws.amazon.com/contact-us/)
- [Security](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html)
- [Compliance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-compliance.html)
- [Changelog](https://docs.aws.amazon.com/AmazonS3/latest/API/WhatsNew.html)
- [Features](undefined)
- [Use Cases](undefined)
- [Integrations](undefined)
- [Integrations](https://aws.amazon.com/marketplace/)

## Maintainers

**FN:** Kin Lane
**Email:** kin@apievangelist.com
**URL:** https://apievangelist.com
