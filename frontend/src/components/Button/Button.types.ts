import { ButtonHTMLAttributes, MouseEvent } from "react";

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  label: string;
  color?: "primary" | "secondary" | "success" | "danger";
  variant?: "contained" | "outlined" | "text";
  disabled?: boolean;
  onClick?: (event: MouseEvent<HTMLButtonElement>) => void;
}
