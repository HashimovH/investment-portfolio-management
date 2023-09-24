

export default function PurchaseModal({ handleCloseModal, stockOptions, handleInputChange, handleSubmit }) {
    return (
        <div className="modal" tabIndex="-1" role="dialog" style={{ display: 'block', backgroundColor: 'rgba(0, 0, 0, 0.5)' }}>
            <div className="modal-dialog" role="document">
                <div className="modal-content">
                    <div className="modal-header">
                        <h5 className="modal-title">Purchase a Stock</h5>
                        <button type="button" className="close btn btn-link" data-dismiss="modal" aria-label="Close" onClick={handleCloseModal}>
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div className="modal-body">
                        <div className="purchase-form">
                            <form onSubmit={handleSubmit}>
                                <div className="form-group mb-3">
                                    <select className="form-control input-bg-gray" id="stockSelect" name="stock_id" placeholder="Stocks" onChange={handleInputChange}>
                                        <option value="" disabled selected>
                                            Choose Stock
                                        </option>
                                        {stockOptions.map((stock, index) => (
                                            <option key={index} value={stock.id}>
                                                {stock.name}
                                            </option>
                                        ))}
                                    </select>
                                </div>
                                <div className="form-group mb-3">
                                    <input type="number" className="form-control input-bg-gray" id="volumeInput" name="volume" placeholder="Volume" onChange={handleInputChange} />
                                </div>
                                <div className="text-end">
                                    <button type="submit" className="btn btn-secondary btn-sm">
                                        Purchase
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}