document.addEventListener("DOMContentLoaded", function () {
    const isbnInput = document.querySelector("#id_isbn");
    if (!isbnInput) return;

    // Create preview button
    const previewBtn = document.createElement("button");
    previewBtn.type = "button";
    previewBtn.textContent = "Load Preview";
    previewBtn.style.marginLeft = "10px";
    isbnInput.parentNode.appendChild(previewBtn);

    // Create preview container
    const previewDiv = document.createElement("div");
    previewDiv.id = "book-preview";
    previewDiv.style.marginTop = "15px";
    isbnInput.parentNode.appendChild(previewDiv);

    // Function to fetch and show preview
    function loadPreview() {
        const isbn = isbnInput.value.trim();
        if (!isbn) {
            alert("Please enter an ISBN first.");
            return;
        }

        fetch(`/admin/books/isbnentry/preview-book/?isbn=${isbn}`)
            .then((res) => res.json())
            .then((data) => {
                if (data.error) {
                    previewDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
                } else {
                    let inventoryInfo = "";
                    if (data.in_inventory) {
                        inventoryInfo = `
                            <p style="color:green; font-weight:bold;">✅ Already in Inventory</p>
                            <p><strong>Price:</strong> ${data.price || "N/A"}</p>
                            <p><strong>Copies:</strong> ${data.copies || 0}</p>
                        `;
                    } else if (data.in_inventory === false) {
                        inventoryInfo = `<p style="color:orange; font-weight:bold;">⚠️ Not in Inventory</p>`;
                    }

                    previewDiv.innerHTML = `
                        <h3>${data.title || "Untitled"}</h3>
                        <p><strong>Author:</strong> ${data.author || "Unknown"}</p>
                        <p><strong>Published:</strong> ${data.published_year || ""}</p>
                        <p><strong>Publisher:</strong> ${data.publisher || ""}</p>
                        <p><strong>Pages:</strong> ${data.page_count || ""}</p>
                        <p><strong>Language:</strong> ${data.language || ""}</p>
                        <p><strong>Categories:</strong> ${data.categories || ""}</p>
                        ${inventoryInfo}
                        <p>${data.description || ""}</p>
                    `;
                }
            })
            .catch((err) => {
                console.error(err);
                previewDiv.innerHTML = `<p style="color:red;">Error loading book preview.</p>`;
            });
    }

    // Hook up button click
    previewBtn.addEventListener("click", loadPreview);

    // Hook up Enter key to trigger preview instead of form submit
    isbnInput.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
            e.preventDefault(); // stop the form from saving
            loadPreview();
        }
    });
});
