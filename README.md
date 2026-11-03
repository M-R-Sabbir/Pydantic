# Pydantic Learning Repository

A hands-on collection of small examples exploring **Pydantic v2**—from the reason for using data models in the first place to validation, derived values, nested data, and serialization.

The examples use patient-shaped data to make the concepts concrete. They are intended for learning, not as a production healthcare application or a source of real patient information.

## What this repository covers

Pydantic lets you describe the shape of Python data with normal type annotations and then validate, normalize, and serialize that data through models. This repository works through that idea progressively:

- Why model-based validation can be clearer and more maintainable than scattered manual `if`/`isinstance` checks.
- `BaseModel` fundamentals and Pydantic's type coercion where values can be safely interpreted as the declared type.
- Common typed fields: `List`, `Dict`, `Optional`, `EmailStr`, and `AnyUrl`.
- Field rules with `Field(...)` and reusable annotation metadata with `Annotated`.
- Derived model values via `@computed_field` (including a BMI-style calculation).
- Nested `BaseModel` classes for structured related data.
- Custom validation with field validators and model validators in `before` and `after` modes.
- Exporting models with `model_dump()` and `model_dump_json()`, including `include` and `exclude` controls.

## Repository structure

```text
.
├── 1.why_pydantic.py       # Manual checks compared with Pydantic models
├── 2.type_validation.ipynb # BaseModel, annotations, and type validation/coercion
├── 3.data_validation.ipynb # Field constraints and Annotated metadata
├── 4.computed_field.py     # Derived fields with @computed_field
├── 5.nested_model.py       # Models composed from other Pydantic models
├── 6.model_validator.ipynb # Field/model validation; before and after modes
└── 7.serialization.py      # Python/JSON serialization and field selection
```

## Getting started

### Prerequisites

- Python 3 installed locally
- `pip`

### Install dependencies

Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install Pydantic v2 with its email-validation extra. The extra is needed for examples that use `EmailStr`.

```bash
python -m pip install "pydantic[email]>=2,<3"
```

To open the notebook examples, install Jupyter as well:

```bash
python -m pip install jupyter
```

## Running the examples

Run the standalone Python examples from the repository root:

```bash
python 1.why_pydantic.py
python 4.computed_field.py
python 5.nested_model.py
python 7.serialization.py
```

Start Jupyter for the notebook lessons:

```bash
jupyter notebook
```

Then open `2.type_validation.ipynb`, `3.data_validation.ipynb`, or `6.model_validator.ipynb` in the browser interface and run the cells in order.

## Learning notes

### 1. Why use Pydantic?

In plain Python, validating a dictionary often means writing and maintaining individual checks for every field, type, and business rule. As a data shape grows, those checks can become repetitive and inconsistent.

With a Pydantic model, the schema, validation rules, and parsing behavior live together:

```python
from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    age: int


patient = Patient(name="Ava", age="32")
```

Here the model declares the intended types and gives Pydantic a single place to validate incoming values. The repository uses this contrast to motivate model-based validation.

### 2. Typed fields and constraints

The notebooks extend basic model fields with collection, optional, contact, and URL types. `Field` and `Annotated` add constraints and descriptive metadata directly beside the type declaration.

```python
from typing import Annotated, Dict, List, Optional
from pydantic import AnyUrl, BaseModel, EmailStr, Field


class PatientContact(BaseModel):
    name: Annotated[str, Field(min_length=1)]
    email: EmailStr
    website: Optional[AnyUrl] = None
    allergies: List[str] = Field(default_factory=list)
    emergency_contact: Dict[str, str] = Field(default_factory=dict)
```

This keeps the data contract readable: someone inspecting the model can see the expected data and its limits without hunting through separate validation functions.

### 3. Computed fields

Some values are derived from validated source fields rather than entered independently. `@computed_field` exposes those values as part of the model output while keeping the calculation close to the data it depends on.

The `computed_field.py` example demonstrates this pattern with a BMI-style derived value.

### 4. Nested models

Real-world data is rarely flat. `nested_model.py` shows how one `BaseModel` can be used as a field inside another, allowing Pydantic to validate the full object tree while keeping each component model focused.

### 5. Custom validators

The validator notebook demonstrates two levels of custom logic:

- **Field validators** validate or transform one field.
- **Model validators** inspect the whole input/model when a rule depends on multiple fields.

`mode="before"` is useful when validation needs to work with raw input before normal parsing. `mode="after"` runs after fields have been validated and is suited to checks involving the completed model state.

### 6. Serialization

Pydantic models can be converted into ordinary Python data or JSON:

```python
data = patient.model_dump()
payload = patient.model_dump_json()
```

The serialization example also demonstrates selecting what is exported with `include` and `exclude`, which is useful when different consumers should receive different parts of a model.

## Suggested learning path

1. Start with `1.why_pydantic.py` to compare manual checking with a model.
2. Work through type validation and field types in `2.type_validation.ipynb`.
3. Add constraints and metadata in `3.data_validation.ipynb`.
4. Explore derived values and object composition in `4.computed_field.py` and `5.nested_model.py`.
5. Move to custom validation logic in `6.model_validator.ipynb`.
6. Finish with `7.serialization.py` to see how validated models leave your application.

## Notes

- The repository is a learning resource focused on Pydantic v2 APIs.
- Values used in examples are illustrative patient data only; they are not real patient records.
- The examples demonstrate validation patterns, not a complete production data-security, privacy, or healthcare-compliance solution.

