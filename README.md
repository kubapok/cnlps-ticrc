
Temporal Image Caption Retrieval Competition
=====================================

Retrieve a caption for a picture from a historical newspaper.

# UPDATES

- March 06, 2023: The baseline has been added. Plase run `baseline.sh` to check it out.
- March 06, 2023: The `test-A` dataset has been published. This is a preliminary test dataset. The final evaluation will be done
on a much bigger dataset published on May 17th. The expected result `expected.tsv` for the `test-A` will not be published.

# Task Description

## Introduction

Multimodal models, especially combining vision and text, are gaining great recognition. A recent example is the image generation model, DALL·E 2 [1]. One such multimodal challenge is Text-Image retrieval, which is to retrieve an image for a text query or retrieve a text for a given image. In this challenge, we introduce a task in the Text-Image retrieval setup, additionally extending the modalities with temporal data.

Language models rarely utilize any input information except for text. E.g additional data could be a text domain, document timestamp, website URL, or other metadata information. However, models trained solely on text data may be limited in usage. Additional temporal information is useful when factual knowledge is required, but the facts change over time (answering the question: “Who is the president of the U.S.A”, “Who was the president of the U.S.A at 1950”), or language semantic changes (word “gay” meaning shifted from “cheerful” to referring homosexuality).

The presented task is based on the Chronicling America [2] and Challenging America [3] projects. Chronicling America is an open database of over 16 million pages of digitized historic American newspapers covering 274 years. Challenging America is a set of temporal challenges built from the Chronicling America dataset.

## Task Definition

The objective is, given a picture from a newspaper and the newspaper's publication daily date, to retrieve a picture caption from a given caption set. Always, exactly one caption is relevant.

## Sample data

**INPUT**:

Image:

[<img src="https://git.wmi.amu.edu.pl/kubapok/cnlps-ticrc/raw/branch/master/sample-picture.png">](https://git.wmi.amu.edu.pl/kubapok/cnlps-ticrc)


Date timestamp: `19280111`

Set of all possible captions: `example caption1`, `example caption2`, `MUTT AND JEFF–  IT TAKES VERY LITTLE TO MAKE JEFF HAPPY`, `example caption3`, …, `last example caption`

**EXPECTED OUTPUT:**

Caption: `MUTT AND JEFF–  IT TAKES VERY LITTLE TO MAKE JEFF HAPPY`

# Data

Data were collected from the Chronicling America dataset and incorporated into the Challenging America project. The test dataset is created from data, which was not previously presented in any Challenging America project. Therefore participants are allowed to use any data from the Challenging America project, but not Chronicling America (as the Chronicling America project site contains test data).

Other Challenging America challenges, which may be useful:
- https://gonito.csi.wmi.amu.edu.pl/challenge/challenging-america-geo-prediction
- https://gonito.csi.wmi.amu.edu.pl/challenge/challenging-america-word-gap-prediction
- https://gonito.csi.wmi.amu.edu.pl/challenge/challenging-america-year-prediction



The dataset is created in the following manner. Pictures and captions are extracted from the newspapers by a human annotator (max. one picture per site).

[<img src="https://git.wmi.amu.edu.pl/kubapok/cnlps-ticrc/raw/branch/master/sample-picture-w-caption.png">](https://git.wmi.amu.edu.pl/kubapok/cnlps-ticrc)


Then, the picture and caption are separated, so the picture does not contain a caption. The caption is typed by a human annotator and kept as golden truth. Newspaper date is taken from newspaper metadata.

All the data is separated into 3 datasets: training (train), development (dev-0), and test (test-A). The newspaper edition does not overlap between these datasets. The exact procedure for generating Challenging America challenges is given in [3].

The final score is calculated only on part of the data released as final test data released on May 17th., not including test data released on Feb 13th.

# Evaluation

## Metric

Metric is Mean Reciprocal Rank ( https://en.wikipedia.org/wiki/Mean_reciprocal_rank ). For the train and development dataset participants are encouraged to use geval evaluation tool, which usage is explained in “HOW TO”.

# Submissions

For a given image id and newspaper date timestamp, participants are expected to return a list of proposed captions sorted descending by probability. Though, always only one caption is relevant.

**In.tsv:**

The first column in the in.tsv dataset is a picture id. The second column in date timestamp in format YYYYMMDD.

**Out.tsv:**

For each row in the in.tsv file, there should be a corresponding list of caption ids sorted from the most probable to the least probable. The ids should be separated by a tab.

Solutions should be submitted to gonito platform.


In order to be included in the final ranking the participants are expected to provide the report that describes their solution. The reports should conform to the requirements specified in the report.tex template and should not exceed 4 pages.


# Baseline

Please run `baseline.sh` from the challenge directory.

# Rules

1. Participants are allowed to use any publicly available pre-trained model.
2. Participants are allowed to use any publicly available data, except for data from the Chronicling America https://chroniclingamerica.loc.gov/ . Using any data available in Challenging America is allowed.
3. It is allowed to use the dev set for the model training.
4. Manual labeling is forbidden.
5. Solutions should be submitted by Gonito platform.
6. Max. 5 solutions per day are allowed.
7. The best scoring solution on the leaderboard on test data is the winning one.
8. Teams may consist of one or more people. There is no restriction on the size of the team. Only one team representative should submit the teams' solution to the platform.
9. If the solution submitted by two different teams is found to be the same, the one who submitted earlier would be ranked higher.
10. To be included in the final ranking, a team should provide a report describing their solution.
11. The report should conform to the requirements specified in the exemplary document provided at <https://github.com/kubapok/cnlps-caiccaic/blob/master/cnlps-report-example.pdf>.


# Special session at FedCSIS 2023

The authors of selected submissions will be invited to prepare the extended versions of their reports for publication in the conference proceedings and presentation at FedCSIS 2023. The selection will be made by Organizing Committee on the basis of final evaluation results, the quality of the submitted reports, and the originality of the presented methods.

# Dates

- Feb 20, 2023: First part of training data available
- Apr 10, 2023: Second part of training data available
- May 17, 2023: Test data available
- May 31, 2023: Deadline for submitting the results
- June 04, 2023: Announcement of the final results, sending invitations for submitting papers
- July 04, 2023: Deadline for submitting invited papers
- July 11, 2023: Author notification
- July 31, 2023: Final paper submission, registration
- Sept 20, 2023: Challenges in Natural Language Processing Symposium

# Organizing Committee

The challenge is organized by the Centre for Artificial Intelligence ( https://csi.amu.edu.pl/ ). The organizing committee is:

- Jakub Pokrywka, Adam Mickiewicz University, Poland
- Piotr Wierzchoń, Adam Mickiewicz University, Poland
- Krzysztof Jassem, Adam Mickiewicz University, Poland
- Kornel Weryszko, Adam Mickiewicz University, Poland


We set up a “CNLPS” Discord server to discuss the the challenge. Please join it to ask any task-related questions: https://discord.gg/VvjHhh7rbF


# Citations

- [1] Ramesh, A., Dhariwal, P., Nichol, A., Chu, C., & Chen, M. (2022). Hierarchical text-conditional image generation with clip latents. arXiv preprint arXiv:2204.06125.
- [2] Lee, B. C. G., Mears, J., Jakeway, E., Ferriter, M., Adams, C., Yarasavage, N., ... & Weld, D. S. (2020). The Newspaper Navigator Dataset: Extracting Headlines and Visual Content from 16 Million Historic Newspaper Pages in Chronicling America. In Proceedings of the 29th ACM International Conference on Information & Knowledge Management (CIKM '20). Association for Computing Machinery, New York, NY, USA, 3055–3062.
- [3] Pokrywka, J., Gralinski, F., Jassem, K., Kaczmarek, K., Jurkiewicz, K., & Wierzchoń, P. (2022, July). Challenging America: Modeling language in longer time scales. In Findings of the Association for Computational Linguistics: NAACL 2022 (pp. 737-749).
