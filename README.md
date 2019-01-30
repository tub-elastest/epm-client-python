[![License badge](https://img.shields.io/badge/license-Apache2-green.svg)](http://www.apache.org/licenses/LICENSE-2.0)
[![Documentation badge](https://img.shields.io/badge/docs-latest-brightgreen.svg)](http://elastest.io/docs/)

[![][ElasTest Logo]][ElasTest]

Copyright © 2017-2019 [ElasTest]. Licensed under [Apache 2.0 License].

epm-client-python
==============================

This repository contains an SDK for python to be used for the ElasTest Platform Manager. Further documentation can be found [here](https://github.com/tub-elastest/epm-client-python/blob/master/docs/index.md).

The ElasTest Platform Manager (EPM) is the interface between the ElasTest testing components (e.g. TORM, Test Support Services, etc.) and the cloud infrastructure where ElasTest is deployed. Hence, this Platform Manager must abstract the cloud services so that ElasTest becomes fully agnostic to them and provide this abstraction via Software Development Toolkits (SDK) or REST APIs to the northbound consumers (i.e. the TORM). The ElasTest Platform Manager enabling ElasTest to be deployed and to execute seamlessly in the target cloud infrastructure that the consortium considers as appropriate (e.g. OpenStack, CloudStack, Mantl, AWS, etc.).

The ElasTest Platform Manager component is currently in development. If you want to contribute to the this project you need to read the [Development documentation](https://github.com/elastest/elastest-platform-manager/blob/master/docs/index.md) 

What is ElasTest
-----------------

This repository is part of [ElasTest], which is an open source elastic platform
aimed to simplify end-to-end testing. ElasTest platform is based on three
principles: i) Test orchestration: Combining intelligently testing units for
creating a more complete test suite following the “divide and conquer” principle.
ii) Instrumentation and monitoring: Customizing the SuT (Subject under Test)
infrastructure so that it reproduces real-world operational behavior and allowing
to gather relevant information during testing. iii) Test recommendation: Using machine
learning and cognitive computing for recommending testing actions and providing
testers with friendly interactive facilities for decision taking.

Documentation
-------------

The [ElasTest] project provides detailed documentation including tutorials,
installation and development guide.

Source
------

Source code for other ElasTest projects can be found in the [GitHub ElasTest
Group].

News
----

Follow us on Twitter @[ElasTest Twitter].

Licensing and distribution
--------------------------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Contribution policy
-------------------

You can contribute to the ElasTest community through bug-reports, bug-fixes,
new code or new documentation. For contributing to the ElasTest community,
you can use the issue support of GitHub providing full information about your
contribution and its value. In your contributions, you must comply with the
following guidelines

* You must specify the specific contents of your contribution either through a
  detailed bug description, through a pull-request or through a patch.
* You must specify the licensing restrictions of the code you contribute.
* For newly created code to be incorporated in the ElasTest code-base, you
  must accept ElasTest to own the code copyright, so that its open source
  nature is guaranteed.
* You must justify appropriately the need and value of your contribution. The
  ElasTest project has no obligations in relation to accepting contributions
  from third parties.
* The ElasTest project leaders have the right of asking for further
  explanations, tests or validations of any code contributed to the community
  before it being incorporated into the ElasTest code-base. You must be ready
  to addressing all these kind of concerns before having your code approved.

Support
-------

The ElasTest project provides community support through the [ElasTest Public
Mailing List] and through [StackOverflow] using the tag *elastest*.


<p align="center">
  <img src="http://elastest.io/images/logos_elastest/ue_logo-small.png"><br>
  Funded by the European Union
</p>

[Apache 2.0 License]: http://www.apache.org/licenses/LICENSE-2.0
[ElasTest]: http://elastest.io/
[ElasTest Blog]: http://elastest.io/blog/
[ElasTest Doc]: http://elastest.io/docs/
[ElasTest Logo]: http://elastest.io/images/logos_elastest/elastest-logo-gray-small.png
[ElasTest Public Mailing List]: https://groups.google.com/forum/#!forum/elastest-users
[ElasTest Twitter]: https://twitter.com/elastestio
[GitHub ElasTest Group]: https://github.com/elastest
[GitHub ElasTest Bugtracker]: https://github.com/elastest/bugtracker
[Repository Doc]: docs/index.md
[StackOverflow]: http://stackoverflow.com/questions/tagged/elastest



