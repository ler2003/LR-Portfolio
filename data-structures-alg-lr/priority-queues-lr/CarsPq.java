/**
 * Lauren Rose Project 3
 * 
 */
package cs1501.p3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.NoSuchElementException;

public class CarsPq implements CarsPqInterface{
    private CarTree vinTree;
    private myHeap priceHeap;
    private myHeap mileageHeap;

    public CarsPq(String filePath){
        vinTree = new CarTree();
        priceHeap = new myHeap();
        mileageHeap = new myHeap();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            br.readLine();
            while ((line = br.readLine()) != null) {
                String[] lines = line.split(":");
                if (lines.length != 6) continue;

                Car car = new Car(
                    lines[0],  // VIN
                    lines[1],  // make
                    lines[2],  // model
                    Integer.parseInt(lines[3]),  // price
                    Integer.parseInt(lines[4]),  // mileage
                    lines[5]   // color
                );
                add(car);
            }
        }
        catch(IOException e){
            System.out.print(e.getMessage());
        }
    }

    /**
     * Add a new Car to the data structure
     * Should throw an `IllegalStateException` if there is already car with the
     * same VIN in the datastructure.
     *
     * @param c Car to be added to the data structure
     */
    @Override
    public void add(Car c) throws IllegalStateException {
        if (vinTree.contains(c.getVIN())) {
            throw new IllegalStateException("Car with VIN " + c.getVIN() + " already exists.");
        }
        vinTree.insert(c);
        priceHeap.insert(c);
        mileageHeap.insert(c);
    }

    /**
     * Retrieve a new Car from the data structure
     * Should throw a `NoSuchElementException` if there is no car with the
     * specified VIN in the datastructure.
     *
     * @param vin VIN number of the car to be updated
     */
    @Override
    public Car get(String vin) throws NoSuchElementException {
        Car car = vinTree.get(vin);
        if (car == null) {
            throw new NoSuchElementException("No car with VIN " + vin + " exists.");
        }
        return car;
    }

    /**
     * Update the price attribute of a given car
     * Should throw a `NoSuchElementException` if there is no car with the
     * specified VIN in the datastructure.
     *
     * @param vin      VIN number of the car to be updated
     * @param newPrice The updated price value
     */
    @Override
    public void updatePrice(String vin, int newPrice) throws NoSuchElementException {
        Car car = get(vin);
        int oldPrice = car.getPrice();
        car.setPrice(newPrice);
        int index = priceHeap.indexOfCarPrice(car);
        if (newPrice < oldPrice) {
            priceHeap.siftUpPrice(index);
        } else {
            priceHeap.siftDownPrice(index);
        }

    }

    /**
     * Update the mileage attribute of a given car
     * Should throw a `NoSuchElementException` if there is not car with the
     * specified VIN in the datastructure.
     *
     * @param vin        VIN number of the car to be updated
     * @param newMileage The updated mileage value
     */
    @Override
    public void updateMileage(String vin, int newMileage) throws NoSuchElementException {
        Car car = get(vin);
        int oldMileage = car.getMileage();
        car.setMileage(newMileage);
        int index = mileageHeap.indexOfCarMileage(car);
        if (newMileage < oldMileage) {
            mileageHeap.siftUpMileage(index);
        } else {
            mileageHeap.siftDownMileage(index);
        }

    }

    /**
     * Update the color attribute of a given car
     * Should throw a `NoSuchElementException` if there is not car with the
     * specified VIN in the datastructure.
     *
     * @param vin      VIN number of the car to be updated
     * @param newColor The updated color value
     */
    @Override
    public void updateColor(String vin, String newColor) throws NoSuchElementException {
        Car car = get(vin);
        car.setColor(newColor);
    }

    /**
     * Remove a car from the data structure
     * Should throw a `NoSuchElementException` if there is not car with the
     * specified VIN in the datastructure.
     *
     * @param vin VIN number of the car to be removed
     */
    @Override
    public void remove(String vin) throws NoSuchElementException {
        Car car = get(vin);
        vinTree.remove(vin);
        priceHeap.remove(car);
        mileageHeap.remove(car);
    }

    /**
     * Get the lowest priced car (across all makes and models)
     * Should return `null` if the data structure is empty
     *
     * @return Car object representing the lowest priced car
     */
    @Override
    public Car getLowPrice() {
        return priceHeap.peekByPrice();
    }

    /**
     * Get the lowest priced car of a given make and model
     * Should return `null` if the data structure is empty
     *
     * @param make  The specified make
     * @param model The specified model
     * 
     * @return Car object representing the lowest priced car
     */
    @Override
    public Car getLowPrice(String make, String model) {
        return vinTree.getLowestPriceByMakeModel(make, model);
    }

    /**
     * Get the car with the lowest mileage (across all makes and models)
     * Should return `null` if the data structure is empty
     *
     * @return Car object representing the lowest mileage car
     */
    @Override
    public Car getLowMileage() {
        return mileageHeap.peekByMileage();
    }

     /**
     * Get the car with the lowest mileage of a given make and model
     * Should return `null` if the data structure is empty
     *
     * @param make  The specified make
     * @param model The specified model
     *
     * @return Car object representing the lowest mileage car
     */
    @Override
    public Car getLowMileage(String make, String model) {
        return vinTree.getLowestMileageByMakeModel(make, model);
    }
}

class CarTree {
    private Node root;
     private class Node {
            Car car;
            int height;
            Node left;
            Node right;

            Node(Car car) {
                this.car = car;
                this.height = 1;
            }
    }

    public void insert(Car car) {
            root = insert(root, car);
    }

    private Node insert(Node node, Car car) {
        if (node == null) {
            return new Node(car);
        }

        int comp = car.getVIN().compareTo(node.car.getVIN());
        if (comp < 0) {
            node.left = insert(node.left, car);
        } 
        else if (comp > 0) {
            node.right = insert(node.right, car);
        } 
        else {
            return node;
        }
        node.height = 1 + Math.max(height(node.left), height(node.right));
        return balance(node);
    }

        public Node balance(Node node) {
            if (balanceFactor(node) > 1) {
                if (balanceFactor(node.left) < 0) {
                    node.left = rotateLeft(node.left);
                }
                node = rotateRight(node);
            } else if (balanceFactor(node) < -1) {
                if (balanceFactor(node.right) > 0) {
                    node.right = rotateRight(node.right);
                }
                node = rotateLeft(node);
            }
            return node;
        }

        private int balanceFactor(Node node) {
            return (node == null) ? 0 : height(node.left) - height(node.right);
        }

        private Node rotateRight(Node toRotate) {
            Node old = toRotate.left;
            Node temp = old.right;

            old.right = toRotate;
            toRotate.left = temp;

            toRotate.height = 1 + Math.max(height(toRotate.left), height(toRotate.right));
            old.height = 1 + Math.max(height(old.left), height(old.right));

            return old;
        }

        private Node rotateLeft(Node toRotate) {
            Node old = toRotate.right;
            Node temp = old.left;

            old.left = toRotate;
            toRotate.right = temp;

            toRotate.height = 1 + Math.max(height(toRotate.left), height(toRotate.right));
            old.height = 1 + Math.max(height(old.left), height(old.right));

            return old;
        }

        private int height(Node node) {
            return (node == null) ? 0 : node.height;
        }

        public boolean contains(String vin) {
            return contains(root, vin);
        }

        private boolean contains(Node node, String vin) {
            if (node == null) {
                return false;
            }

            int cmp = vin.compareTo(node.car.getVIN());
            if (cmp < 0) {
                return contains(node.left, vin);
            } 
            else if (cmp > 0) {
                return contains(node.right, vin);
            } 
            else {
                return true;
            }
        }

        public Car get(String vin) {
            Node node = get(root, vin);
            return (node == null) ? null : node.car;
        }

        private Node get(Node node, String vin) {
            if (node == null) {
                return null;
            }

            int cmp = vin.compareTo(node.car.getVIN());
            if (cmp < 0) {
                return get(node.left, vin);
            } 
            else if (cmp > 0) {
                return get(node.right, vin);
            } 
            else {
                return node;
            }
        }

        public void remove(String vin) {
            root = remove(root, vin);
        }

        private Node remove(Node node, String vin) {
            if (node == null) {
                return null;
            }

            int cmp = vin.compareTo(node.car.getVIN());
            if (cmp < 0) {
                node.left = remove(node.left, vin);
            } 
            else if (cmp > 0) {
                node.right = remove(node.right, vin);
            } 
            else {
                if (node.left == null) {
                    return node.right;
                } 
                else if (node.right == null) {
                    return node.left;
                }

                Node temp = node;
                node = min(temp.right);
                node.right = deleteMin(temp.right);
                node.left = temp.left;
            }

            node.height = 1 + Math.max(height(node.left), height(node.right));
            return balance(node);
        }

        public Car peek() {
            return min(root).car;
        }

        private Node min(Node node) {
            if (node.left == null) return node;
            else return min(node.left);
        }


        private Node deleteMin(Node node) {
            if (node.left == null) return node.right;
            node.left = deleteMin(node.left);
            return balance(node);
        }

        public Car getLowestPriceByMakeModel(String make, String model) {
            return getLowestByMakeModel(root, make, model, true);
        }

        public Car getLowestMileageByMakeModel(String make, String model) {
            return getLowestByMakeModel(root, make, model, false);
        }

        private Car getLowestByMakeModel(Node node, String make, String model, boolean mileageOrPrice) {
            if (node == null) {
                return null;
            }
            Car current = (node.car.getMake().equals(make) && node.car.getModel().equals(model)) ? node.car : null;
            if(mileageOrPrice){ //If true, search for price
                Car left = getLowestByMakeModel(node.left, make, model, true);
                Car right = getLowestByMakeModel(node.right, make, model, true);
                return minCarPrice(minCarPrice(left, right), current);
            }
            else{ //If false, search for mileage
                Car left = getLowestByMakeModel(node.left, make, model, false);
                Car right = getLowestByMakeModel(node.right, make, model, false);
                return minCarMileage(minCarMileage(left, right), current);
            }
        }

      private Car minCarPrice(Car a, Car b) {
            if (a == null) return b;
            if (b == null) return a;
            return a.getPrice() < b.getPrice() ? a : b; 
        }

        private Car minCarMileage(Car a, Car b) {
            if (a == null) return b;
            if (b == null) return a;
            return a.getMileage() < b.getMileage() ? a : b; 
        }
}

class myHeap {
    private Car[] mileageHeap;
    private Car[] priceHeap;
    private int size;
    private static final int INITIAL_CAPACITY = 10;

    public myHeap() {
        this.mileageHeap = new Car[INITIAL_CAPACITY];
        this.priceHeap = new Car[INITIAL_CAPACITY];
        this.size = 0;
    }

    public void insert(Car car) {
        checkSize();
        mileageHeap[size] = car;
        priceHeap[size] = car;
        siftUpMileage(size);
        siftUpPrice(size);
        size++;
    }
    public Car peekByMileage() {
        if (size == 0) {
            return null;
        }
        return mileageHeap[0];
    }
    public Car peekByPrice() {
        if (size == 0) {
            return null;
        }
        return priceHeap[0];
    }


    public void remove(Car car) {
        int indexM = indexOfCarMileage(car);
        int indexP = indexOfCarPrice(car);
        mileageHeap[indexM] = mileageHeap[size - 1];
        priceHeap[indexP] = priceHeap[size - 1];
        size--;
        siftDownMileage(indexM);
        siftDownPrice(indexP);
    }

    public void checkSize() {
        if (size == mileageHeap.length) {
            mileageHeap = resizeHeap(mileageHeap);
            priceHeap = resizeHeap(priceHeap);
        }
    }

    private Car[] resizeHeap(Car[] original) {
        Car[] newHeap = new Car[original.length * 2];
        System.arraycopy(original, 0, newHeap, 0, original.length);
        return newHeap;
    }

    public void siftUpMileage(int index) {
        while (index > 0) {
            int upIndex = ((index - 1) / 2);
            if (mileageHeap[index].getMileage() < mileageHeap[upIndex].getMileage()) {
                swap(mileageHeap, index, upIndex);
                index = upIndex;
            } 
            else {
                break;
            }
        }
    }

    public void siftUpPrice(int index) {
        while (index > 0) {
            int upIndex = ((index - 1) / 2);
            if (priceHeap[index].getPrice() < priceHeap[upIndex].getPrice()) {
                swap(priceHeap, index, upIndex);
                index = upIndex;
            } 
            else {
                break;
            }
        }
    }

    public void siftDownMileage(int index) {
        int leftIndex = (2 * (index + 1));
        int rightIndex = (2 * (index + 2));
        int smallest = index;

        if (leftIndex < size && mileageHeap[leftIndex].getMileage() < mileageHeap[smallest].getMileage()) {
            smallest = leftIndex;
        }

        if (rightIndex < size && mileageHeap[rightIndex].getMileage() < mileageHeap[smallest].getMileage()) {
            smallest = rightIndex;
        }

        if (smallest != index) {
            swap(mileageHeap, index, smallest);
            siftDownMileage(smallest);
        }
    }

    public void siftDownPrice(int index) {
        int leftIndex = (2 * (index + 1));
        int rightIndex = (2 * (index + 2));
        int smallest = index;

        if (leftIndex < size && priceHeap[leftIndex].getPrice() < priceHeap[smallest].getPrice()) {
            smallest = leftIndex;
        }

        if (rightIndex < size && priceHeap[rightIndex].getPrice() < priceHeap[smallest].getPrice()) {
            smallest = rightIndex;
        }

        if (smallest != index) {
            swap(priceHeap, index, smallest);
            siftDownPrice(smallest);
        }
    }

    private void swap(Car[] heap, int i, int j) {
        Car temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }
    public int indexOfCarMileage(Car car) {
        for (int i = 0; i < size; i++) {
            if (mileageHeap[i].equals(car)) {
                return i;
            }
        }
        return -1;
    }

    public int indexOfCarPrice(Car car) {
        for (int i = 0; i < size; i++) {
            if (priceHeap[i].equals(car)) {
                return i;
            }
        }
        return -1;
    }

}