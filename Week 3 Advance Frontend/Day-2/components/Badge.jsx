export default function Badge({
  children,
  variant = "default",
  className = "",
}) {
  const baseStyles =
    "inline-flex items-center px-2 py-1 text-xs font-medium rounded";

  const variants = {
    default: "bg-gray-200 text-gray-800",
    primary: "bg-blue-600 text-white",
    success: "bg-green-600 text-white",
    warning: "bg-yellow-400 text-black",
    danger: "bg-red-600 text-white",
  };

  return (
    <span className={`${baseStyles} ${variants[variant]} ${className}`}>
      {children}
    </span>
  );
}
