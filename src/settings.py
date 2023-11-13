from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "ISIC 2017: Part 3 - Disease Classification Task"
PROJECT_NAME_FULL: str = "ISIC 2017: Part 3 - Disease Classification Task"
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC0_1_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Medical()]
CATEGORY: Category = Category.Medical()

CV_TASKS: List[CVTask] = [CVTask.Classification()]
ANNOTATION_TYPES: List[AnnotationType] = []

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2017

HOMEPAGE_URL: str = "https://challenge.isic-archive.com/landing/2017/44/"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 8514121
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/isic-2017-part-3"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = "https://challenge.isic-archive.com/data/#2017"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = ["https://arxiv.org/abs/1710.05006"]
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = None

CITATION_URL: Optional[str] = "https://arxiv.org/abs/1710.05006"
AUTHORS: Optional[List[str]] = [
    "Noel C. F. Codella",
    "David Gutman",
    "M. Emre Celebi",
    "Brian Helba",
    "Michael A. Marchetti",
    "Stephen W. Dusza",
    "Aadi Kalloo",
    "Konstantinos Liopyris",
    "Nabin Mishra",
    "Harald Kittler",
    "Allan Halpern"
]
AUTHORS_CONTACTS: Optional[List[str]] = None

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "IBM T. J. Watson Research Center", "Emory University", 
    "University of Central Arkansas", "Kitware", 
    "Memorial Sloan-Kettering Cancer Center", 
    "Missouri University of Science and Technology, USA", 
    "Medical University of Vienna, Austria"
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://research.ibm.com/labs/watson/", 
    "https://www.emory.edu/home/index.html", 
    "https://uca.edu/", 
    "https://www.kitware.com/", 
    "https://www.mskcc.org/", 
    "https://www.mst.edu/", 
    "https://www.meduniwien.ac.at/web/en/"
]

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "groups for first binary classification task": ["melanoma","nevus_or_seborrheic_keratosis"],
    "groups for second classification task":["seborrheic_keratosis", "melanoma_or_nevus"],
    "__POSTTEXT__": "Also, the dataset contains ***age_approximate*** and ***sex*** tags"
}
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
