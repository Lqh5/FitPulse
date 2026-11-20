/**
 * Posture Correction Page — 用户端页面 3
 * Issue #8 (张智轩)
 */
export default function CorrectionPage() {
  return (
    <div className="page-container">
      <header className="bg-brand-500 text-white px-4 py-3 sticky top-0 z-10">
        <h1 className="font-semibold">Posture Correction</h1>
      </header>

      <div className="p-4">
        {/* Upload area */}
        <div className="border-2 border-dashed border-brand-300 rounded-xl p-8 text-center">
          <p className="text-4xl mb-4">📷</p>
          <p className="font-medium text-gray-700 mb-2">
            Upload a photo of your exercise posture
          </p>
          <p className="text-sm text-gray-400 mb-4">
            AI will analyze your form and give feedback
          </p>
          <div className="flex gap-3 justify-center">
            <button className="btn-primary text-sm">📸 Take Photo</button>
            <button className="btn-primary text-sm">🖼️ Choose from Gallery</button>
          </div>
        </div>

        {/* History placeholder */}
        <div className="mt-8">
          <h2 className="font-medium text-gray-700 mb-4">Correction History</h2>
          <p className="text-center text-gray-400 text-sm">No corrections yet</p>
        </div>
      </div>
    </div>
  );
}