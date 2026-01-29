## Week 4 (Day 3) - High Performance Rest API and Advance Query Engine

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To build a Product API which should be containing the Dynamic Search Engine , Dynamic queries that include filtering, sorting and pagination, soft delete functionality for the Products also the error handling.

## Query

**search -**
Performed Regex search **($regex)** on the product name

**filters -**
Added filters for Minimum and Maximum Price for a Product.

**softDelete -**
Added soft delete parameter in schema **deletedAt** which can be assigned to true or null with Current Time.

**pagination**
Added pagination to limit the records of Products

**Dynamic Queries**
Made the Queries Dynamic to give user the option for the filter, sortby and limit option.

```text
async findMany({ filter, sort, limit }) {
return Product.find(filter).sort(sort).limit(limit);
}
```

## Error Handling

Added error-handling middleware where I used the global error format.

## Learning

By performing this task I learned about the Core Architecture of backend development and how they work like:

- 3 Layer Architecture (Controller -> Service Layer -> Data Access Layer) also the separation of concerns(SOC) between them.
- Advanced MongoDB Querying: $regex, sorting, filtering, pagination
- Importance of SoftDelete
- Also the Error Handling
