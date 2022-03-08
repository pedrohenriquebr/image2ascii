import { useContext, useEffect, useRef, useState } from 'react'
import { ImageUploadServiceContext } from '../../services/image-upload.service'

import './Home.scss'
import './loader.css'

const MAXIMUM_WIDTH = 200
const MAXIMUM_HEIGHT = 200

const clampDimensions = (width: number, height: number) => {
  if (height > MAXIMUM_HEIGHT) {
    const reducedWidth = Math.floor((width * MAXIMUM_HEIGHT) / height)
    return [reducedWidth, MAXIMUM_HEIGHT]
  }

  if (width > MAXIMUM_WIDTH) {
    const reducedHeight = Math.floor((height * MAXIMUM_WIDTH) / width)
    return [MAXIMUM_WIDTH, reducedHeight]
  }

  return [width, height]
}

export default function Home() {
  const service = useContext(ImageUploadServiceContext)
  const canvasRef = useRef<HTMLCanvasElement | null>(null)
  const [width, setWidth] = useState(0)
  const [height, setHeight] = useState(0)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    if (canvasRef.current) {
      setWidth(canvasRef.current.width)
      setHeight(canvasRef.current.height)
    }
  }, [canvasRef])

  function handleSubmit(ev: any) {
    ev.preventDefault()
    setLoading(true)
    const file = document.querySelector('#file')
    file &&
      //@ts-ignore
      service?.uploadImage(file.files[0], 60*5,48*5).then((d) => {
        const el = document.querySelector('.result-image')

        console.log(d.ascii_body)
        const rs = d.ascii_body
        //@ts-ignore
        el.textContent = rs
        setLoading(false)
      })
  }

  function handleImage(e: any) {
    var reader = new FileReader()
    reader.onload = function (event) {
      var img = new Image()
      img.onload = function () {
        if (!canvasRef || !canvasRef.current) return
        const [width, height] = clampDimensions(img.width, img.height)

        canvasRef.current.width = width
        canvasRef.current.height = height
        canvasRef.current.getContext('2d')?.drawImage(img, 0, 0, width, height)
        setWidth(width)
        setHeight(height)
      }
      //@ts-ignore
      img.src = event.target.result
    }
    reader.readAsDataURL(e.target.files[0])
  }

  return (
    <div>
      <div className="main">
        <div className="result">
          <canvas ref={canvasRef}></canvas>
        </div>
        <form method="post" action="uploadfile">
          <input
            onChange={handleImage}
            type="file"
            name="fileupload"
            id="file"
          />
          <button onClick={handleSubmit} type="submit">
            Submit
          </button>
        </form>
      </div>
      Result:
      <pre className="result-image"></pre>

      {loading && (
        <>
          <div className={`loader ${loading ? 'active' : ''}`} />{' '}
          <div className="loader-background"></div>
        </>
      )}
    </div>
  )
}
