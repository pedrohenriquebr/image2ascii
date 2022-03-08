import './Button.module.scss'
import { ButtonProps } from './Button.types'

export function Button({
  label,
  color = 'primary',
  disabled = false,
  variant = 'contained',
  ...props
}: ButtonProps) {
  return <button {...props}>Click me</button>
}
