package cs1501.p3;

import java.util.NoSuchElementException;

/**
 * CarsPq specification interface for CS1501 Project 3
 * @author Dr. Farnan
 * @author Dr. Garrison
 */
interface CarsPqInterface {

    /**
     * Adds a new Car to the data structure. Throws an `IllegalStateException` if there is already
     * car with the same VIN in the data structure.
     *
     * @param c Car to be added to the data structure
     * @throws IllegalStateException if c is a car with duplicate VIN
     */
    public void add(Car c) throws IllegalStateException;

    /**
     * Retrieves the Car from the data structure with the given VIN. Throws a
     * `NoSuchElementException` if there is no car with the specified VIN in the data structure.
     *
     * @param vin VIN number of the car to be retrieved
     * @return the car in the data structure with the given VIN
     * @throws NoSuchElementException if no car is found with the given VIN
     */
    public Car get(String vin) throws NoSuchElementException;

    /**
     * Updates the price attribute of a given car. Throws a `NoSuchElementException` if there is no
     * car with the specified VIN in the data structure.
     *
     * @param vin VIN number of the car to be updated
     * @param newPrice The updated price value
     * @throws NoSuchElementException if no car is found with the given VIN
     */
    public void updatePrice(String vin, int newPrice) throws NoSuchElementException;

    /**
     * Updates the mileage attribute of a given car. Throws a `NoSuchElementException` if there is
     * not car with the specified VIN in the data structure.
     *
     * @param vin VIN number of the car to be updated
     * @param newMileage The updated mileage value
     * @throws NoSuchElementException if no car is found with the given VIN
     */
    public void updateMileage(String vin, int newMileage) throws NoSuchElementException;

    /**
     * Updates the color attribute of a given car. Throws a `NoSuchElementException` if there is not
     * car with the specified VIN in the data structure.
     *
     * @param vin VIN number of the car to be updated
     * @param newColor The updated color value
     * @throws NoSuchElementException if no car is found with the given VIN
     */
    public void updateColor(String vin, String newColor) throws NoSuchElementException;

    /**
     * Removes a car from the data structure. Throws a `NoSuchElementException` if there is not car
     * with the specified VIN in the data structure.
     *
     * @param vin VIN number of the car to be removed
     * @throws NoSuchElementException if no car is found with the given VIN
     */
    public void remove(String vin) throws NoSuchElementException;

    /**
     * Retrieves and returns the lowest priced car (across all makes and models). Returns `null` if
     * the data structure is empty.
     *
     * @return Car object representing the lowest priced car, or null if the structure is empty
     */
    public Car getLowPrice();

    /**
     * Retrieves and returns the lowest priced car of the given make and model. Returns `null` if
     * the make and model is not found (including if the data structure is empty).
     *
     * @param make The specified make
     * @param model The specified model
     * @return Car object representing the lowest priced car of the given make and model, or null if
     * the make and model is not found
     */
    public Car getLowPrice(String make, String model);

    /**
     * Retrieves and returns the car with the lowest mileage (across all makes and models). Returns
     * `null` if the data structure is empty.
     *
     * @return Car object representing the lowest mileage car, or null if the structure is empty
     */
    public Car getLowMileage();

    /**
     * Retrieves and returns the car with the lowest mileage of the given make and model. Returns
     * `null` if the make and model is not found (including if the data structure is empty).
     *
     * @param make The specified make
     * @param model The specified model
     * @return Car object representing the lowest mileage car of the given make and model, or null
     * if the make and model is not found
     */
    public Car getLowMileage(String make, String model);
}
