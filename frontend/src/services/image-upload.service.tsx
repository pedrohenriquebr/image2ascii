import { createContext } from 'react'
import { ImageUploadResult } from '../models/home.model'
import * as api from './api'

export interface IImageUploadService {
  uploadImage(file: File, width: number, height: number): Promise<ImageUploadResult>
}

export const ImageUploadServiceContext = createContext<IImageUploadService | null>(
  null,
)

const ImageUploadService = ({ children }: any) => {
  const service = {
    async uploadImage(file: File, width: number = 1280, height: number = 720): Promise<ImageUploadResult> {
      var formData = new FormData()
      formData.append('upload', file)
      formData.append('max_width', width.toString())
      formData.append('max_height', height.toString())
      const body = await api.instance.post('uploadfile', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })

      return body.data as ImageUploadResult
    },
  }

  return (
    <>
      <ImageUploadServiceContext.Provider value={service}>
        {children}
      </ImageUploadServiceContext.Provider>
    </>
  )
}

export default ImageUploadService
