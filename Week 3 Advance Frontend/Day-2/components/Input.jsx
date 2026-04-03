export default function Input({
  type = "text",
  placeholder,
  value,
  onChange,
  variant = "default",
  className = "",
  ...props
}) {
  const baseStyles = "transition-colors duration-200 focus:outline-none";

  const variants = {
    default: "border-gray-300 focus:ring-blue-500 focus:border-blue-500",
    search: "bg-white text-black text-sm focus:outline-none",
  };

  return (
    <input
      type={type}
      placeholder={placeholder}
      value={value}
      onChange={onChange}
      className={`${baseStyles} ${variants[variant]} ${className}`}
      {...props}
    />
  );
}
