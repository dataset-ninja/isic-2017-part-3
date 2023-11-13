The **ISIC 2017: Part 3 - Disease Classification Task** dataset is tailored for a classification task in the domain of dermatology. Comprising a total of 2750 images, the dataset presents two distinct binary classification tasks. The first task involves discriminating between ***nevus_or_seborrheic_keratosis***, encompassing 2229 images, and ***melanoma***, consisting of 521 images. The second task requires classification between ***melanoma_or_nevus***, with 2364 images, and ***seborrheic_keratosis***, containing 386 images. Participants in this task are tasked with independently addressing these two binary image classification challenges, each centered around three distinctive diagnoses of skin lesions: melanoma, nevus, and seborrheic keratosis. The dataset serves as a valuable resource for advancing the development and evaluation of algorithms dedicated to dermatological disease classification.

## About ISIC 2017 Challenge

The International Skin Imaging Collaboration (ISIC) has begun to aggregate a large-scale publicly accessible dataset of dermoscopy images. Currently, the dataset houses more than 20,000 images from leading clinical centers internationally, acquired from a variety of devices used at each center. The ISIC dataset was the foundation for the first public benchmark challenge on dermoscopic image analysis in 2016. 

The goal of the challenge is to help participants develop image analysis tools to enable the automated diagnosis of melanoma from dermoscopic images. Image analysis of skin lesions is composed of 3 parts:

- Part 1: Lesion Segmentation [(Available on DatasetNinja)](https://datasetninja.com/isic-2017-part-1)
- Part 2: Detection and Localization of Visual Dermoscopic Features/Patterns
- Part 3: Disease Classification (current)  

For each, data consisted of images and corresponding ground truth annotations, split into training (n=2000), validation (n=150), and holdout test (n=600) datasets. Predictions could be submitted on validation and test datasets. The validation submissions provided instantaneous feedback in the form of performance evaluations, as well as ranking in comparison to other participants. Test submissions only provided feedback after the submission deadline.

# About Disease Classification Task

In this task, participants are asked to complete two independent binary image classification tasks that involve three unique diagnoses of skin lesions (melanoma, nevus, and seborrheic keratosis). In the first binary classification task, participants are asked to distinguish between melanoma and nevus and seborrheic keratosis. In the second binary classification task, participants are asked to distinguish between seborrheic keratosis and nevus and melanoma.

- Melanoma – malignant skin tumor, derived from melanocytes (melanocytic)
- Nevus – benign skin tumor, derived from melanocytes (melanocytic)
- Seborrheic keratosis – benign skin tumor, derived from keratinocytes (non-melanocytic)

<img width="800" alt="ISIC2017-part3-preview" src="https://github.com/dataset-ninja/isic-2017-part-3/assets/123257559/2cd29890-ee63-4d45-bbf1-d5d870244842">

<span style="font-size: smaller; font-style: italic;"> Example images from “Part 3: Disease Classification.” Ground truth labels written above.</span>
