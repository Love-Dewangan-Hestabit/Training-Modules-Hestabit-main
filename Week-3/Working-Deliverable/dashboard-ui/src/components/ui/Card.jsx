export default function Card({
  title,
  children,
  variant = "primary",
  footer,
  className = "",
}) {
  const variants = {
    gray1: "bg-gray-900 text-white",

    gray2: "bg-gray-800 text-white",
    gray3: "bg-gray-700 text-white",

    gray4: "bg-gray-600 text-white",
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
