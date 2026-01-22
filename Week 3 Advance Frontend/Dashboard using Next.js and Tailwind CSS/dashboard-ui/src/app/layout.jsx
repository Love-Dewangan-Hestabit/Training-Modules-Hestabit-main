import "./globals.css";

export const metadata = {
  title: {
    default: "FitBit – Fitness That Fits You",
    template: "%s | FitBit",
  },
  description:
    "FitBit helps you train smarter, stay consistent, and achieve your fitness goals.",
  viewport: "width=device-width, initial-scale=1",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="bg-white">{children}</body>
    </html>
  );
}
