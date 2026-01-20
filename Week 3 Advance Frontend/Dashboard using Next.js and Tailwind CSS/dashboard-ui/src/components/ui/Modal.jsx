"use client";

export default function Modal({ isOpen, onClose, title, children, footer }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg shadow-xl max-w-md w-full mx-4">
        <div className="border-b px-6 py-4 flex items-center justify-between">
          <h3 className="text-xl font-semibold text-gray-800">{title}</h3>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 text-2xl"
          >
            ×
          </button>
        </div>
        <div className="px-6 py-4">{children}</div>
        {footer && (
          <div className="border-t px-6 py-4 flex justify-end gap-2">
            {footer}
          </div>
        )}
      </div>
    </div>
  );
}
