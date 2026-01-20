export default function Badge({
  children,
  variant = "primary",
  className = "",
}) {
  const variants = {
    primary: "bg-blue-100 text-blue-800",
    warning: "bg-yellow-100 text-yellow-800",
    success: "bg-green-100 text-green-800",
    danger: "bg-red-100 text-red-800",
  };

  return (
    <span
      className={`px-2 py-1 rounded text-xs font-medium ${variants[variant]} ${className}`}
    >
      {children}
    </span>
  );
}
