# Service Orders Management - Pennsylvania American Water

## Overview
Feature to track, manage, and modify scheduled service appointments and technician visits.

**Menu Location:** Main Menu > Service Requests > Service Orders

---

## 1. Service Orders List (Dashboard)

### Page Header
- Title: "My Service Orders"
- Filter button (top right)
- Create new service request button (links to existing service request forms)

### Filter Options (Slide-out panel)
- Status (multi-select):
  - All
  - Scheduled
  - En Route
  - In Progress
  - Completed
  - Cancelled
- Service Type (multi-select):
  - All
  - Meter Reading
  - Meter Installation/Replacement
  - Leak Investigation
  - Service Connection
  - Disconnection/Reconnection
  - Water Quality Testing
  - Emergency Repair
  - Other
- Date Range (presets + custom):
  - Upcoming (next 30 days)
  - Past 30 Days
  - Past 90 Days
  - Custom Range
- Account (dropdown if multiple accounts)

### Service Order Cards (Mobile) / Table (Desktop)

**Card/Row Display:**
- Work Order # (e.g., WO-2024-12345)
- Status Badge (color coded):
  - Scheduled (blue)
  - En Route (orange)
  - In Progress (purple)
  - Completed (green)
  - Cancelled (gray)
- Service Type
- Scheduled Date & Time
- Service Address
- Technician Name (if assigned)
- Quick Actions:
  - View Details button
  - Modify Appointment (if scheduled/not started)
  - Cancel (if scheduled/not started)

### Empty State
- "No service orders found"
- Button: "Schedule a Service Request"

---

## 2. Service Order Details Page

### Header Section
- Work Order Number
- Large Status Badge
- Account Number
- Service Address
- Print/Download button (PDF service report)

### Status Timeline (Visual Progress Tracker)
- Requested (date/time) ✓
- Scheduled (date/time) ✓
- Confirmed (date/time) ✓
- En Route (date/time, if applicable)
- In Progress (date/time, if applicable)
- Completed (date/time, if applicable)

### Appointment Details Card
- Service Type
- Scheduled Date
- Scheduled Time Window (e.g., 8:00 AM - 12:00 PM)
- Estimated Duration (e.g., 1-2 hours)
- Priority Level: Standard / Urgent / Emergency
- Actions:
  - Modify Appointment button
  - Cancel Appointment button
  - Add to Calendar button (iCal/Google Calendar)

### Technician Information Card (When assigned)
- Technician Name
- Photo (if available)
- Phone Number (click to call)
- Estimated Arrival Time (if en route)
- Live Status: "John is on the way" / "John has arrived" / "John is working on your service"

### Service Details Card
- Description of Work Requested
- Special Instructions (customer provided)
- Preparation Required (e.g., "Please ensure access to meter location")
- Access Instructions (gate codes, parking info)

### Work Completed Card (After service completed)
- Work Performed (technician notes)
- Parts/Equipment Used
- Meter Reading (if applicable)
- Before Photos (if applicable)
- After Photos (if applicable)
- Technician Signature
- Customer Signature (if required)
- Completion Date/Time
- Total Time on Site

### Charges Card (If applicable)
- Service Fee
- Parts Cost
- Labor Cost
- Total Amount
- Payment Status
- Invoice Number (link to download)

### Customer Feedback Section (After completion)
- Rate Your Experience (1-5 stars)
- How was the technician? (1-5 stars)
- Comments (optional)
- Submit Feedback button

### Communication Log
- Timeline of all communications:
  - SMS notifications sent
  - Email confirmations
  - Customer notes added
  - Status changes
  - Rescheduling history

---

## 3. Modify Appointment Flow

### Step 1: Current Appointment
- Display current date/time
- Reason for change (dropdown):
  - Need different date/time
  - Will not be available
  - Emergency resolved
  - Other
- Continue button

### Step 2: Select New Date & Time
- Calendar picker (show next 30 days)
- Available time slots displayed for selected date:
  - Morning (8 AM - 12 PM)
  - Afternoon (12 PM - 5 PM)
  - Specific slots if available (e.g., 9-11 AM, 1-3 PM)
- Show technician availability
- Unavailable dates/times grayed out

### Step 3: Confirm Changes
- Show old vs new appointment:
  - Original: [date/time]
  - New: [date/time]
- Updated Contact Info:
  - Phone (pre-filled, editable)
  - Email (pre-filled, editable)
- Additional notes (optional)
- Checkbox: "Send me SMS reminders"
- Checkbox: "Send me email reminders"

### Step 4: Confirmation
- "Appointment Updated Successfully"
- New work order number (if system generates new one)
- Confirmation details
- Email/SMS confirmation sent
- Add to calendar button
- Return to Service Orders button

---

## 4. Cancel Appointment Flow

### Cancellation Form
- Work Order Number (display only)
- Scheduled Date/Time (display only)
- Reason for Cancellation (dropdown):
  - No longer needed
  - Resolved issue myself
  - Scheduling conflict
  - Emergency resolved
  - Cost concerns
  - Other
- Additional Comments (optional text area)
- Warning message: "Cancelling this appointment may delay service. Consider rescheduling instead."
- Buttons:
  - "Reschedule Instead" (goes to modify flow)
  - "Cancel Appointment" (red button)

### Cancellation Confirmation
- "Appointment Cancelled"
- Cancellation number for reference
- Show cancelled appointment details
- Email confirmation sent
- Options:
  - Schedule New Appointment button
  - Return to Service Orders
  - Contact Customer Service (if they have questions)

---

## 5. Notifications & Reminders

### SMS Notifications (opt-in)
- Appointment confirmed (immediate)
- Reminder 24 hours before
- Technician assigned
- Technician is on the way (30 min before arrival)
- Technician has arrived
- Service completed
- Feedback request

### Email Notifications
- Appointment confirmation with details
- Appointment reminder (24 hours)
- Appointment modified confirmation
- Cancellation confirmation
- Service completion summary with PDF report
- Feedback request

### Push Notifications (if mobile app)
- Real-time status updates
- Technician location updates
- Estimated arrival time changes

---

## 6. Additional Features (Industry Best Practices)

### Emergency Service Orders
- Priority flag for urgent/emergency requests
- Expedited scheduling (next available, same-day if possible)
- Emergency contact number prominently displayed
- Escalation option if not resolved in timeframe

### Service Order History
- Searchable archive of all past service orders
- Filter by service type, date, technician
- Download past service reports
- View patterns (e.g., recurring issues)

### Recurring Service Orders
- For regular maintenance (meter readings, inspections)
- Auto-schedule next appointment
- Standing instructions saved
- Preferred technician (if available)

### Photo Documentation
- Customer can upload photos when creating request
- Technician can add before/after photos
- Photo gallery in service order details
- Timestamp and location data on photos

### Service Area Map
- Show service address on map
- Technician location (if en route/on site)
- Nearby affected areas (if related to outages)

### Integration Points
- Link to related outages (if service needed due to outage)
- Link to account billing (if charges apply)
- Link to transaction history (payment for services)
- Link to water quality reports (if quality testing performed)

### Accessibility Features
- Screen reader compatible
- High contrast mode
- Large text option
- Keyboard navigation
- Multiple language support (if needed)

---

## UI Design Elements (Following App System Design)

### Colors for Status
- Scheduled: Blue (#2196F3)
- En Route: Orange (#FF9800)
- In Progress: Purple (#9C27B0)
- Completed: Green (#4CAF50)
- Cancelled: Gray (#9E9E9E)
- Emergency: Red (#F44336)

### Card Layout
- Consistent with other app sections
- White background
- Subtle shadow
- Rounded corners
- Clear typography hierarchy
- Icon usage for quick identification

### Responsive Design
- Mobile: Stacked cards, bottom sheets for actions
- Tablet: 2-column layout for list, side panel for details
- Desktop: Table view with expandable rows or side panel details

### Interactive Elements
- Click-to-call phone numbers
- Click-to-map addresses
- Swipe to cancel/modify (mobile)
- Drag-to-refresh list
- Auto-refresh status (every 30 seconds when active)

---

## Technical Considerations

### API Endpoints (suggested)
```
GET /api/service-orders?accountId={id}&status={status}&startDate={date}
GET /api/service-orders/{orderId}
PUT /api/service-orders/{orderId}/reschedule
DELETE /api/service-orders/{orderId}/cancel
GET /api/service-orders/{orderId}/available-slots?date={date}
POST /api/service-orders/{orderId}/feedback
GET /api/service-orders/{orderId}/report (PDF)
POST /api/service-orders/{orderId}/notifications/preferences
```

### Data Refresh
- Auto-refresh every 30 seconds for active orders (En Route, In Progress)
- Pull-to-refresh on mobile
- Real-time updates via websocket for status changes (optional)

### Performance
- Pagination for service order list (25 per page)
- Lazy loading of photos
- Cache service order details
- Offline mode for viewing completed orders

### Security
- Verify account ownership before displaying orders
- Require authentication for modifications
- Audit trail for all changes
- PCI compliance for payment information (if applicable)
