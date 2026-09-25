# Virtual Parameter XML File Schema

The Virtual Parameter `.vpx` file is an XML file with the structure described below.

The file has a **Header** section, which contains the information displayed during a file preview, and a **Data** section, which contains the conversion and parameter definitions.

## Structure

| Element | Contents |
|---|---|
| `VirtualParameters` | Root element. Contains `Header` and `Data`. |
| `Header` | `ModifiedOn` (dd/mm/yyyy hh:mm:ss), `ModifiedBy`, `BuildNumber` (System Monitor build), optional `Description` and `Notes`, and `AppSet`. |
| `AppSet` / `App` | One `App` per Application: `ID` (hexadecimal, for example `0x0001`), `Name`, `Version` and `Build`. |
| `Data` | Attribute `Name`. Contains `ConvRules` and `Parameters`. |
| `ConvRules` | The conversions used by the Virtual Parameters: `RationalFunction`, `TableEnum`, `TextEnum` and `FreeFunction` elements. Each starts with `Name`, followed by the optional `Description`, `Format`, `Units` and `Default`. |
| `RationalFunction` | `Coeffs`, containing the six coefficients `a` to `f` of the [rational conversion](../parameter-properties/conversions/rational-conversion.md). |
| `TableEnum` | `Interpolated` (`Yes` or `No`), then one `Enum` per mapping, each with `EnumIdx` (raw value) and `EnumIdy` (engineering value). |
| `TextEnum` | One `Enum` per mapping, each with `EnumIdx` (raw value, hexadecimal) and `EnumText`. |
| `FreeFunction` | `Expression` elements holding the formula and inverse of a [formula conversion](../parameter-properties/conversions/formula-conversion.md). |
| `Parameters` / `Parameter` | One `Parameter` per Virtual Parameter (see below). |

Each `Parameter` contains, in this order:

| Element | Description |
|---|---|
| `Type` | Always `Virtual Measurement`. |
| `Name` | The parameter Name. |
| `Identifier` | Written only when it differs from the Name. |
| `Group` / `GroupDescription` | The group path (levels separated by `\`) and the group description. |
| `DataType` | For example `UBYTE`, `SWORD`, `ULONG`, `FLOAT` or `FLOAT64`. |
| `Conversion` | The name of the conversion. |
| `Properties` | `Description`, `ByteOrder` (`MSB_FIRST` or `MSB_LAST`), `Format` (format override), `Min` and `Max` (engineering limits), `BitMask` and `ReadOnlyFlags`. |
| `Display` | `Resolution`, `Accuracy`, `MaxRefreshScaling`, `MaxRefresh`, `ErrorMask`, `DisplayMin` and `DisplayMax` (warning limits), `Colour` (trace colour), `Under` and `Over` (`LIMIT_1` or `LIMIT_2`), `TraceType` (`DIGITAL` or `LOGICAL`; omitted for linear), `BitShift` and `ShiftDirection` (`Left` or `Right`), `DisplayOffset`, `ArraySize`, `ChannelId`, `BlockOffset`, `MinLoggingScaling`, `MinLogging` and `MinLoggingEnabled` (`True` or `False`). |
| `Units` | Units override. |
| `Expression` | The formula of the Virtual Parameter. See [Mathematical Operators](../parameter-properties/mathematical-operators.md). |

Most elements are written only when they have a value or differ from the default.

## Schema

```xml
<?xml version="1.0"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" attributeFormDefault="unqualified" elementFormDefault="qualified">
  <xs:complexType name="ConvCommon">
    <xs:sequence>
      <xs:element type="xs:string" name="Name"/>
      <xs:element type="xs:string" name="Description" minOccurs="0"/>
      <xs:element type="xs:string" name="Format" minOccurs="0"/>
      <xs:element type="xs:string" name="Units" minOccurs="0"/>
      <xs:element type="xs:string" name="Default" minOccurs="0"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="VirtualParameters">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="Header">
          <xs:complexType>
            <xs:sequence>
              <xs:element type="xs:string" name="ModifiedOn" minOccurs="0"/>
              <xs:element type="xs:string" name="ModifiedBy" minOccurs="0"/>
              <xs:element type="xs:int" name="BuildNumber" minOccurs="0"/>
              <xs:element type="xs:string" name="Description" minOccurs="0"/>
              <xs:element type="xs:string" name="Notes" minOccurs="0"/>
              <xs:element name="AppSet" minOccurs="0">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="App" minOccurs="0" maxOccurs="unbounded">
                      <xs:complexType>
                        <xs:sequence>
                          <xs:element type="xs:string" name="ID"/>
                          <xs:element type="xs:string" name="Name"/>
                          <xs:element type="xs:string" name="Version"/>
                          <xs:element type="xs:string" name="Build" minOccurs="0"/>
                        </xs:sequence>
                      </xs:complexType>
                    </xs:element>
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name="Data">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="ConvRules" minOccurs="0">
                <xs:complexType>
                  <xs:choice minOccurs="0" maxOccurs="unbounded">
                    <xs:element name="RationalFunction">
                      <xs:complexType>
                        <xs:complexContent>
                          <xs:extension base="ConvCommon">
                            <xs:sequence>
                              <xs:element name="Coeffs">
                                <xs:complexType>
                                  <xs:sequence>
                                    <xs:element type="xs:double" name="a"/>
                                    <xs:element type="xs:double" name="b"/>
                                    <xs:element type="xs:double" name="c"/>
                                    <xs:element type="xs:double" name="d"/>
                                    <xs:element type="xs:double" name="e"/>
                                    <xs:element type="xs:double" name="f"/>
                                  </xs:sequence>
                                </xs:complexType>
                              </xs:element>
                            </xs:sequence>
                          </xs:extension>
                        </xs:complexContent>
                      </xs:complexType>
                    </xs:element>
                    <xs:element name="TableEnum">
                      <xs:complexType>
                        <xs:complexContent>
                          <xs:extension base="ConvCommon">
                            <xs:sequence>
                              <xs:element type="xs:string" name="Interpolated"/>
                              <xs:element name="Enum" minOccurs="0" maxOccurs="unbounded">
                                <xs:complexType>
                                  <xs:sequence>
                                    <xs:element type="xs:double" name="EnumIdx"/>
                                    <xs:element type="xs:double" name="EnumIdy"/>
                                  </xs:sequence>
                                </xs:complexType>
                              </xs:element>
                            </xs:sequence>
                          </xs:extension>
                        </xs:complexContent>
                      </xs:complexType>
                    </xs:element>
                    <xs:element name="TextEnum">
                      <xs:complexType>
                        <xs:complexContent>
                          <xs:extension base="ConvCommon">
                            <xs:sequence>
                              <xs:element name="Enum" minOccurs="0" maxOccurs="unbounded">
                                <xs:complexType>
                                  <xs:sequence>
                                    <xs:element type="xs:string" name="EnumIdx"/>
                                    <xs:element type="xs:string" name="EnumText"/>
                                  </xs:sequence>
                                </xs:complexType>
                              </xs:element>
                            </xs:sequence>
                          </xs:extension>
                        </xs:complexContent>
                      </xs:complexType>
                    </xs:element>
                    <xs:element name="FreeFunction">
                      <xs:complexType>
                        <xs:complexContent>
                          <xs:extension base="ConvCommon">
                            <xs:sequence>
                              <xs:element type="xs:string" name="Expression" minOccurs="0" maxOccurs="2"/>
                            </xs:sequence>
                          </xs:extension>
                        </xs:complexContent>
                      </xs:complexType>
                    </xs:element>
                  </xs:choice>
                </xs:complexType>
              </xs:element>
              <xs:element name="Parameters" minOccurs="0">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="Parameter" minOccurs="0" maxOccurs="unbounded">
                      <xs:complexType>
                        <xs:sequence>
                          <xs:element type="xs:string" name="Type"/>
                          <xs:element type="xs:string" name="Name" minOccurs="0"/>
                          <xs:element type="xs:string" name="Identifier" minOccurs="0"/>
                          <xs:element type="xs:string" name="Group" minOccurs="0"/>
                          <xs:element type="xs:string" name="GroupDescription" minOccurs="0"/>
                          <xs:element type="xs:string" name="DataType" minOccurs="0"/>
                          <xs:element type="xs:string" name="Conversion" minOccurs="0"/>
                          <xs:element name="Properties">
                            <xs:complexType>
                              <xs:sequence>
                                <xs:element type="xs:string" name="Description" minOccurs="0"/>
                                <xs:element type="xs:string" name="ByteOrder" minOccurs="0"/>
                                <xs:element type="xs:string" name="Format" minOccurs="0"/>
                                <xs:element type="xs:double" name="Min" minOccurs="0"/>
                                <xs:element type="xs:double" name="Max" minOccurs="0"/>
                                <xs:element type="xs:string" name="BitMask" minOccurs="0"/>
                                <xs:element type="xs:string" name="ReadOnlyFlags" minOccurs="0"/>
                              </xs:sequence>
                            </xs:complexType>
                          </xs:element>
                          <xs:element name="Display">
                            <xs:complexType>
                              <xs:sequence>
                                <xs:element type="xs:int" name="Resolution" minOccurs="0"/>
                                <xs:element type="xs:double" name="Accuracy" minOccurs="0"/>
                                <xs:element type="xs:int" name="MaxRefreshScaling" minOccurs="0"/>
                                <xs:element type="xs:int" name="MaxRefresh" minOccurs="0"/>
                                <xs:element type="xs:string" name="ErrorMask" minOccurs="0"/>
                                <xs:element type="xs:double" name="DisplayMin" minOccurs="0"/>
                                <xs:element type="xs:double" name="DisplayMax" minOccurs="0"/>
                                <xs:element type="xs:string" name="Colour" minOccurs="0"/>
                                <xs:element type="xs:string" name="Under" minOccurs="0"/>
                                <xs:element type="xs:string" name="Over" minOccurs="0"/>
                                <xs:element type="xs:string" name="TraceType" minOccurs="0"/>
                                <xs:element type="xs:int" name="BitShift" minOccurs="0"/>
                                <xs:element type="xs:string" name="ShiftDirection" minOccurs="0"/>
                                <xs:element type="xs:double" name="DisplayOffset" minOccurs="0"/>
                                <xs:element type="xs:int" name="ArraySize" minOccurs="0"/>
                                <xs:element type="xs:int" name="ChannelId" minOccurs="0"/>
                                <xs:element type="xs:int" name="BlockOffset" minOccurs="0"/>
                                <xs:element type="xs:int" name="MinLoggingScaling" minOccurs="0"/>
                                <xs:element type="xs:int" name="MinLogging" minOccurs="0"/>
                                <xs:element type="xs:string" name="MinLoggingEnabled" minOccurs="0"/>
                              </xs:sequence>
                            </xs:complexType>
                          </xs:element>
                          <xs:element type="xs:string" name="Units" minOccurs="0"/>
                          <xs:element type="xs:string" name="Expression" minOccurs="0"/>
                        </xs:sequence>
                      </xs:complexType>
                    </xs:element>
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
            <xs:attribute type="xs:string" name="Name"/>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

**See also:** [Virtual Parameter Files](virtual-parameter-files.md); [Virtual Parameters Import/Export](virtual-parameters-import-export.md)
