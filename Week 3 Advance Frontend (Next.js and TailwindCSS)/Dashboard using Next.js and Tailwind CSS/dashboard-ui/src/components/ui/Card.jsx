export default function Card({
  title,
  children,
  variant = "primary",
  footer,
  className = "",
}) {
  const variants = {
    primary: "bg-blue-600 text-white",
    warning: "bg-yellow-500 text-white",
    success: "bg-green-600 text-white",
    danger: "bg-red-600 text-white",
  };

  return (
    <div className={`rounded-lg shadow-md overflow-hidden ${className}`}>
      <div className={`p-4 ${variants[variant]}`}>
        <h3 className="text-lg font-semibold">{title}</h3>
      </div>
      <div className="p-4 bg-white">{children}</div>
      {footer && (
        <div
          className={`p-3 ${variants[variant]} flex items-center justify-between text-sm`}
        >
          {footer}
        </div>
      )}
    </div>
  );
}
