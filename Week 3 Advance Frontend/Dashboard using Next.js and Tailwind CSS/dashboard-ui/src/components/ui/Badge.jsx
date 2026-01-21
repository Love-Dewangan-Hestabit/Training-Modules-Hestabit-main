export default function Badge({
  children,
  variant = "primary",
  className = "",
}) {
  const variants = {
    blue: "bg-blue-100 text-blue-800",
    yellow: "bg-yellow-100 text-yellow-800",
    green: "bg-green-100 text-green-800",
    red: "bg-red-100 text-red-800",
  };

  return (
    <span
      className={`px-2 py-1 rounded text-xs font-medium ${variants[variant]} ${className}`}
    >
      {children}
    </span>
  );
}
