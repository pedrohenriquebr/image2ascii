import os
from hashlib import sha256

from fastapi import File, Form, HTTPException, UploadFile
from config import TEMP_DIR
from core.image2ascii import toascii,DENSITY
from services import logger


async def upload_image(upload: UploadFile = File(...),
                       max_width: int = File(80),
                       max_height: int = Form(40),
                       force_resize: bool = Form(False),
                       density: str = Form(DENSITY)):

    if upload.content_type not in ["image/jpeg", "image/png"]:
        logger.error(f"{upload.filename} is not a valid image file.")
        raise HTTPException(status_code=415)

    logger.info('Uploading file: %s', upload.filename)
    logger.info(f'Parameters -> max_width: {max_width}, ' +
                f'max_height: {max_height}, ' +
                f'density: {density}')

    content = upload.file.read()
    sha256_ = sha256(content).hexdigest()
    with open(os.path.join(TEMP_DIR, sha256_), 'wb') as f:
        f.write(content)

    ascii_body = toascii(os.path.join(TEMP_DIR, sha256_),
                         density=density, max_width=max_width,
                         force_resize=force_resize,
                         max_height=max_height)
    size = len(content)

    logger.info('File uploaded: %s', upload.filename)
    logger.info('File size: %s', size)
    logger.info('SHA256: %s', sha256_)

    return {"filename": upload.filename,
            "content_type": upload.content_type,
            "size": size,
            "ascii_body": ascii_body}
