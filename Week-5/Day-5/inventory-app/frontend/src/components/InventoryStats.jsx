export default function InventoryStats({ products }) {
  const totalProducts = products.length;
  const totalQuantity = products.reduce((sum, p) => sum + p.quantity, 0);
  const totalValue = products.reduce((sum, p) => sum + p.quantity * p.price, 0);

  return (
    <div className="stats">
      <div className="stat">📦 Products: {totalProducts}</div>
      <div className="stat">🔢 Quantity: {totalQuantity}</div>
      <div className="stat">💰 Value: ₹{totalValue}</div>
    </div>
  );
}
