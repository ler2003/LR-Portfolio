document.addEventListener('DOMContentLoaded', () => {
    const baseURL = 'http://localhost:3000/smartphones';
    document.getElementById('viewAllBtn').addEventListener('click', async () => {
        try {
            console.log('getting smartphones');
            const response = await fetch(baseURL);
            if (!response.ok) {
                throw new Error(`error: ${response.status}`);
            }
            const smartphones = await response.json();
            console.log('Smartphones:', smartphones);
            const list = document.getElementById('smartphoneList');
            list.innerHTML = '';
            smartphones.forEach(phone => {
                const li = document.createElement('li');
                li.textContent = `ID: ${phone.id}, Brand: ${phone.brand}, Price: $${phone.price}`;
                list.appendChild(li);
            });
        } catch (error) {
            console.error('error getting smartphones:', error);
        }
    });

    document.getElementById('viewSmartphoneBtn').addEventListener('click', async () => {
        const id = document.getElementById('viewSmartphoneId').value;
        if (!id) {
            alert('enter an ID.');
            return;
        }
        try {
            console.log(`getting smartphone ID: ${id}...`);
            const response = await fetch(`${baseURL}/${id}`);
            if (!response.ok) {
                throw new Error(`error: ${response.status}`);
            }
            const phone = await response.json();
            console.log('smartphone details:', phone);
            const details = document.getElementById('smartphoneDetails');
            details.innerHTML = `
                <p>Brand: ${phone.brand}</p>
                <p>Price: $${phone.price}</p>
                <p>Screen: ${phone.screen}</p>
                <p>Pixels: ${phone.pixels}</p>
                <p>Resolution: ${phone.resolution}</p>
                <p>Storage: ${phone.storage}</p>
                <p>Ram: ${phone.ram}</p>
                <p>Battery: ${phone.battery}</p>
                <p>Weight: ${phone.weight}g</p>
            `;
            document.getElementById('viewSmartphoneId').value = '';
        } catch (error) {
            console.error('error getting smartphone details:', error);
        }
    });

    document.getElementById('addSmartphoneBtn').addEventListener('click', async () => {
        const brand = document.getElementById('newBrand').value;
        const price = document.getElementById('newPrice').value;
        const screen = document.getElementById('newScreen').value;
        const pixels = document.getElementById('newPixels').value;
        const resolution = document.getElementById('newResolution').value;
        const storage = document.getElementById('newStorage').value;
        const ram = document.getElementById('newRam').value;
        const battery = document.getElementById('newBattery').value;
        const weight = document.getElementById('newWeight').value;

        if (!brand || !price || !screen || !pixels || !resolution || !storage || !ram || !battery || !weight) {
            alert('fill in all the fields please thanks');
            return;
        }

        const newPhone = { brand, price, screen, pixels, resolution, storage, ram, battery, weight };

        try {
            console.log('adding new smartphone:', newPhone);
            await fetch(baseURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newPhone)
            });

            document.getElementById('newBrand').value = '';
            document.getElementById('newPrice').value = '';
            document.getElementById('newScreen').value = '';
            document.getElementById('newPixels').value = '';
            document.getElementById('newResolution').value = '';
            document.getElementById('newStorage').value = '';
            document.getElementById('newRam').value = '';
            document.getElementById('newBattery').value = '';
            document.getElementById('newWeight').value = '';
        } catch (error) {
            console.error('error adding smartphone:', error);
        }
    });
    document.getElementById('updateSmartphoneBtn').addEventListener('click', async () => {
        const id = document.getElementById('updateId').value;
        const brand = document.getElementById('updateBrand').value;
        const price = document.getElementById('updatePrice').value;
        const screen = document.getElementById('updateScreen').value;
        const pixels = document.getElementById('updatePixels').value;
        const resolution = document.getElementById('updateResolution').value;
        const storage = document.getElementById('updateStorage').value;
        const ram = document.getElementById('updateRam').value;
        const battery = document.getElementById('updateBattery').value;
        const weight = document.getElementById('updateWeight').value;

        if (!id) {
            alert('enter an ID');
            return;
        }

        const updatedFields = {};
        if (brand) updatedFields.brand = brand;
        if (price) updatedFields.price = price;
        if (screen) updatedFields.screen = screen;
        if (pixels) updatedFields.pixels = pixels;
        if (resolution) updatedFields.resolution = resolution;
        if (storage) updatedFields.storage = storage;
        if (ram) updatedFields.ram = ram;
        if (battery) updatedFields.battery = battery;
        if (weight) updatedFields.weight = weight;

        try {
            console.log(`updating ID: ${id} with fields:`, updatedFields);
            await fetch(`${baseURL}/${id}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(updatedFields)
            });

            document.getElementById('updateId').value = '';
            document.getElementById('updateBrand').value = '';
            document.getElementById('updatePrice').value = '';
            document.getElementById('updateScreen').value = '';
            document.getElementById('updatePixels').value = '';
            document.getElementById('updateResolution').value = '';
            document.getElementById('updateStorage').value = '';
            document.getElementById('updateRam').value = '';
            document.getElementById('updateBattery').value = '';
            document.getElementById('updateWeight').value = '';
        } catch (error) {
            console.error('error updating smartphone:', error);
        }
    });
    document.getElementById('deleteSmartphoneBtn').addEventListener('click', async () => {
        const id = document.getElementById('deleteId').value;

        if (!id) {
            alert('enter ID');
            return;
        }

        try {
            console.log(`deleting smartphone ID: ${id}`);
            await fetch(`${baseURL}/${id}`, {
                method: 'DELETE'
            });

            document.getElementById('deleteId').value = '';
        } catch (error) {
            console.error('error deleting smartphone:', error);
        }
    });
});

