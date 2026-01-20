export default function Card({
  title,
  children,
  variant = "primary",
  footer,
  className = "",
}) {
  const variants = {
    blue: "bg-blue-600 text-white",

    yellow: "bg-yellow-500 text-white",
    green: "bg-green-600 text-white",

    red: "bg-red-600 text-white",
  };

  return (
    <div className={`rounded-lg shadow-md overflow-hidden ${className}`}>
      <div className={`p-4 ${variants[variant]} border-b-2 border-white/20`}>
        <h3 className="text-lg font-semibold">{title}</h3>
      </div>

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
