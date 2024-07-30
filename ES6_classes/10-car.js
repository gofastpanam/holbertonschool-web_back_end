class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const Constructor = Object.getPrototypeOf(this).constructor;
    return new Constructor(this._brand, this._motor, this._color);
  }
}

export default Car;
