package cs1501.p3;

/**
 * Car specification interface for CS1501 Project 3
 * @author Dr. Farnan
 * @author Dr. Garrison
 */
interface CarInterface {

    /**
     * Retrieves the VIN attribute
     *
     * @return the VIN
     */
    public String getVIN();

    /**
     * Retrieves the make attribute
     *
     * @return the make
     */
    public String getMake();

    /**
     * Retrieves the model attribute
     *
     * @return the model
     */
    public String getModel();

    /**
     * Retrieves the price attribute
     *
     * @return the price
     */
    public int getPrice();

    /**
     * Retrieves the mileage attribute
     *
     * @return the mileage
     */
    public int getMileage();

    /**
     * Retrieves the color attribute
     *
     * @return The color
     */
    public String getColor();

    /**
     * Updates the price attribute
     *
     * @param newPrice the new price
     */
    public void setPrice(int newPrice);

    /**
     * Updates the mileage attribute
     *
     * @param newMileage the new mileage
     */
    public void setMileage(int newMileage);

    /**
     * Updates the color attribute
     *
     * @param newColor the new color
     */
    public void setColor(String newColor);

}

