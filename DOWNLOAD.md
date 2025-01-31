Dataset **ISIC 2017: Part 3 - Disease Classification Task** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzI5NTRfSVNJQyAyMDE3OiBQYXJ0IDMgLSBEaXNlYXNlIENsYXNzaWZpY2F0aW9uIFRhc2svaXNpYy0yMDE3Oi1wYXJ0LTMtLS1kaXNlYXNlLWNsYXNzaWZpY2F0aW9uLXRhc2stRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiZncrNnhjc05YL053RUxhTy82cU1uZWYrTVVaaVUzRE1GM2w0bytDKzFEbz0ifQ==)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='ISIC 2017: Part 3 - Disease Classification Task', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://challenge.isic-archive.com/data/#2017).