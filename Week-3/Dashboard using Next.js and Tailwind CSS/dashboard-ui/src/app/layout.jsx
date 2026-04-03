import "./globals.css";

export const metadata = {
  title: {
    default: "FitBit – Fitness That Fits You",
    template: "%s | FitBit",
  },
  description:
    "FitBit helps you train smarter, stay consistent, and achieve your fitness goals.",
};

export const viewport = {
  width: "device-width",
  initialScale: 1,
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="bg-white">{children}</body>
    </html>
  );
}
