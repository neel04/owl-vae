def get_loader(data_id: str, batch_size: int, filepath: str | list[str] | None = None):
    if data_id == "mnist":
        from . import mnist
        return mnist.get_loader(batch_size)
    if data_id == "local_imagenet_256":
        from . import local_imagenet_256
        return local_imagenet_256.get_loader(batch_size)
    if data_id == "s3_imagenet":
        from . import imagenet
        return imagenet.get_loader(batch_size)
    if data_id == "local_cod":
        from . import local_cod
        return local_cod.get_loader(batch_size)
    if data_id == "audio_loader":
        from .audio_loader import get_audio_loader
        assert filepath is not None, "No filepath provided for the dataset."
        return get_audio_loader(batch_size, filepath)
