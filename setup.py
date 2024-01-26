import setuptools

__Version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "Tilak Akasapu"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "tilak57233@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version= __Version__,
    author = AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Simple TextSummarizer using Transformers NLP",
    url = "https://github.com/Tilakakasapu/Text_Summarization_NLPProject.git",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)