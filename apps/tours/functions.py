MODEL_NAME = 'guides'

def guide_image_dir(instance, filename):
    return MODEL_NAME+f"/{instance.name}/{filename}"