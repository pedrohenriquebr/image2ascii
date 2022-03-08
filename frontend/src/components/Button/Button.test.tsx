import { render, screen } from '@testing-library/react'
import { Button } from './Button'

it('renders learn react link', () => {
  render(<Button label="learn react" />)
  const linkElement = screen.getByText(/learn react/i)
  expect(linkElement).toBeInTheDocument()
})
