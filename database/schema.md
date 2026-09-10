# CampusCare Database Schema

## Core Tables

### 1. users
Stores every person who can use CampusCare.

| Field | Description |
|---|---|
| id | Unique user ID |
| name | Full name |
| email | College email address |
| password_hash | Secure encrypted password |
| role | student, organizer, or admin |
| created_at | Account creation date and time |

### 2. events
Stores college events created by organizers.

| Field | Description |
|---|---|
| id | Unique event ID |
| title | Event name |
| description | Event details |
| category | Event type |
| start_time | Event start date and time |
| end_time | Event end date and time |
| venue | Event location |
| capacity | Maximum number of participants |
| organizer_id | User who created the event |
| status | draft, pending, approved, cancelled, or completed |

### 3. registrations
Connects students with the events they register for.

| Field | Description |
|---|---|
| id | Unique registration ID |
| student_id | Registered student |
| event_id | Selected event |
| status | registered, cancelled, or waitlisted |
| registered_at | Registration date and time |

## Relationships

- One organizer (`users`) can create many events (`events`).
- One student (`users`) can have many registrations (`registrations`).
- One event (`events`) can have many registrations (`registrations`).
- Each registration belongs to exactly one student and one event.

## Important Rules

- A student can register only once for the same event.
- Registrations cannot exceed an event’s capacity.
- When capacity is full, the registration status becomes `waitlisted`.
- A student cannot register for overlapping events.
- Only organizers and administrators can create or edit events.