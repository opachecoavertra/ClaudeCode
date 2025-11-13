# Lovable Prompt: Bulk Transactions & Outages Monitoring

## Overview
Add a new menu option in the main navigation for **"Transactions & Outages"** that allows customers to view bulk transactions and monitor outages reports with real-time status tracking for Pennsylvania American Water services.

## Feature Structure

### Main Menu Item
**Title:** Transactions & Outages
**Icon:** Activity/Chart icon combined with alert/warning icon
**Location:** Main navigation menu (top level)
**Route:** `/transactions-outages`

## Page Layout

The page should have two main sections accessible via tabs or side-by-side panels:

### Section 1: Bulk Transactions
**Purpose:** Allow customers to view all transaction history across their accounts in one consolidated view

### Section 2: Outages & Status Tracking
**Purpose:** Monitor service outages, planned maintenance, and track resolution status in real-time

---

## Section 1: Bulk Transactions Details

### Overview
Display a comprehensive, filterable table of all transactions across customer accounts with export capabilities.

### Key Features

1. **Transaction Table**
   - Sortable columns (Date, Account, Transaction Type, Amount, Status)
   - Search functionality
   - Date range picker (Last 7 days, Last 30 days, Last 90 days, Custom range)
   - Export to CSV/PDF options
   - Pagination (25, 50, 100 items per page)

2. **Transaction Filters**
   - **By Account:** Multi-select dropdown
   - **By Transaction Type:** Payment, Adjustment, Credit, Refund, Late Fee, Service Charge
   - **By Status:** Completed, Pending, Failed, Reversed
   - **By Service Type:** Water, Wastewater, Both
   - **By Amount Range:** Min/Max amount inputs

3. **Summary Cards** (Display at top of section)
   - Total Transactions (current filter)
   - Total Amount (current filter)
   - Pending Transactions Count
   - Last Transaction Date

### Mock Data Structure

**Accounts to Reference:**
- Account #1234-5678-W (Residential - Water Only) - 123 Main St, Pittsburgh, PA
- Account #2345-6789-WW (Residential - Water & Wastewater) - 456 Oak Ave, Philadelphia, PA
- Account #3456-7890-C (Commercial - Water Only) - 789 Business Blvd, Harrisburg, PA
- Account #4567-8901-WW (Commercial - Water & Wastewater) - 321 Industrial Dr, Allentown, PA

**Sample Transactions Data:**

```javascript
[
  {
    id: "TXN-2024-001234",
    date: "2024-11-10",
    accountNumber: "1234-5678-W",
    accountName: "John Smith - 123 Main St",
    type: "Payment",
    serviceType: "Water",
    amount: -85.32,
    status: "Completed",
    paymentMethod: "Auto-Pay",
    confirmationNumber: "CONF-948573"
  },
  {
    id: "TXN-2024-001235",
    date: "2024-11-09",
    accountNumber: "2345-6789-WW",
    accountName: "Sarah Johnson - 456 Oak Ave",
    type: "Payment",
    serviceType: "Water & Wastewater",
    amount: -142.67,
    status: "Completed",
    paymentMethod: "Credit Card",
    confirmationNumber: "CONF-948574"
  },
  {
    id: "TXN-2024-001236",
    date: "2024-11-08",
    accountNumber: "3456-7890-C",
    accountName: "ABC Corp - 789 Business Blvd",
    type: "Service Charge",
    serviceType: "Water",
    amount: 450.00,
    status: "Completed",
    paymentMethod: "ACH",
    confirmationNumber: "CONF-948575"
  },
  {
    id: "TXN-2024-001237",
    date: "2024-11-07",
    accountNumber: "1234-5678-W",
    accountName: "John Smith - 123 Main St",
    type: "Credit",
    serviceType: "Water",
    amount: -25.00,
    status: "Completed",
    paymentMethod: "H2O Help Program",
    confirmationNumber: "CONF-948576"
  },
  {
    id: "TXN-2024-001238",
    date: "2024-11-06",
    accountNumber: "4567-8901-WW",
    accountName: "XYZ Industries - 321 Industrial Dr",
    type: "Payment",
    serviceType: "Water & Wastewater",
    amount: -1250.45,
    status: "Pending",
    paymentMethod: "Check",
    confirmationNumber: "PENDING"
  },
  {
    id: "TXN-2024-001239",
    date: "2024-11-05",
    accountNumber: "2345-6789-WW",
    accountName: "Sarah Johnson - 456 Oak Ave",
    type: "Late Fee",
    serviceType: "Water & Wastewater",
    amount: 15.00,
    status: "Completed",
    paymentMethod: "Auto-Applied",
    confirmationNumber: "CONF-948577"
  },
  {
    id: "TXN-2024-001240",
    date: "2024-11-04",
    accountNumber: "3456-7890-C",
    accountName: "ABC Corp - 789 Business Blvd",
    type: "Adjustment",
    serviceType: "Water",
    amount: -75.00,
    status: "Completed",
    paymentMethod: "Billing Correction",
    confirmationNumber: "CONF-948578"
  },
  {
    id: "TXN-2024-001241",
    date: "2024-11-03",
    accountNumber: "1234-5678-W",
    accountName: "John Smith - 123 Main St",
    type: "Refund",
    serviceType: "Water",
    amount: -50.00,
    status: "Pending",
    paymentMethod: "Check Mailed",
    confirmationNumber: "PENDING"
  }
]
```

### Visual Design Suggestions
- Use a clean, modern data table with alternating row colors
- Color-code transaction types (green for payments/credits, red for fees/charges, blue for adjustments)
- Status badges with appropriate colors (green for completed, yellow for pending, red for failed)
- Responsive table that converts to cards on mobile
- Loading skeleton while data fetches
- Empty state with helpful message when no transactions match filters

---

## Section 2: Outages & Status Tracking Details

### Overview
Real-time monitoring dashboard for service outages, planned maintenance, and status updates.

### Key Features

1. **Interactive Outage Map**
   - Pennsylvania map showing affected areas
   - Color-coded by severity (Red: Critical, Orange: Moderate, Yellow: Minor)
   - Click regions for details
   - Toggle between Water and Wastewater services

2. **Active Outages List**
   - Real-time status updates
   - Affected areas and customer count
   - Estimated restoration time
   - Type of outage (Emergency, Planned Maintenance, Water Quality Issue)
   - Progress timeline

3. **Status Filters**
   - **By Status:** All, Investigating, In Progress, Resolved
   - **By Type:** Emergency Repair, Planned Maintenance, Water Quality, System Pressure
   - **By Service:** Water, Wastewater
   - **By Area:** Dropdown with Pennsylvania regions

4. **Alert Preferences**
   - Subscribe to notifications for your area
   - Email/SMS toggle
   - Notification types selection

### Mock Data Structure

**Sample Outages Data:**

```javascript
[
  {
    id: "OUT-2024-0456",
    reportedDate: "2024-11-13 06:30 AM",
    lastUpdated: "2024-11-13 08:15 AM",
    type: "Emergency Repair",
    serviceType: "Water",
    severity: "Critical",
    status: "In Progress",
    affectedArea: "Downtown Pittsburgh",
    affectedZipCodes: ["15222", "15219"],
    affectedCustomers: 1250,
    address: "400 Grant St, Pittsburgh, PA",
    description: "Water main break causing service disruption. Crews on site performing emergency repairs.",
    estimatedRestoration: "2024-11-13 02:00 PM",
    timeline: [
      {
        timestamp: "2024-11-13 06:30 AM",
        status: "Reported",
        message: "Issue reported by multiple customers"
      },
      {
        timestamp: "2024-11-13 07:00 AM",
        status: "Investigating",
        message: "Crew dispatched to location"
      },
      {
        timestamp: "2024-11-13 07:45 AM",
        status: "In Progress",
        message: "Water main break confirmed. Excavation in progress"
      },
      {
        timestamp: "2024-11-13 08:15 AM",
        status: "In Progress",
        message: "Water shut off to affected area. Repair work underway"
      }
    ],
    relatedAccounts: ["1234-5678-W"]
  },
  {
    id: "OUT-2024-0457",
    reportedDate: "2024-11-12 02:00 PM",
    lastUpdated: "2024-11-12 06:30 PM",
    type: "Planned Maintenance",
    serviceType: "Wastewater",
    severity: "Moderate",
    status: "Resolved",
    affectedArea: "South Philadelphia",
    affectedZipCodes: ["19145", "19148"],
    affectedCustomers: 850,
    address: "Wastewater Treatment Plant - S Broad St",
    description: "Scheduled maintenance on wastewater pumping station completed successfully.",
    estimatedRestoration: "2024-11-12 06:00 PM",
    timeline: [
      {
        timestamp: "2024-11-05 09:00 AM",
        status: "Scheduled",
        message: "Maintenance scheduled for Nov 12"
      },
      {
        timestamp: "2024-11-12 02:00 PM",
        status: "In Progress",
        message: "Maintenance work began"
      },
      {
        timestamp: "2024-11-12 06:30 PM",
        status: "Resolved",
        message: "Maintenance completed. All systems operational"
      }
    ],
    relatedAccounts: ["2345-6789-WW"]
  },
  {
    id: "OUT-2024-0458",
    reportedDate: "2024-11-13 09:00 AM",
    lastUpdated: "2024-11-13 09:30 AM",
    type: "Water Quality",
    serviceType: "Water",
    severity: "Minor",
    status: "Investigating",
    affectedArea: "Allentown East",
    affectedZipCodes: ["18103"],
    affectedCustomers: 450,
    address: "Region: East Allentown Distribution",
    description: "Reports of discolored water. Testing in progress. Water is safe to drink.",
    estimatedRestoration: "2024-11-13 12:00 PM",
    timeline: [
      {
        timestamp: "2024-11-13 09:00 AM",
        status: "Reported",
        message: "Multiple reports of discolored water received"
      },
      {
        timestamp: "2024-11-13 09:30 AM",
        status: "Investigating",
        message: "Water quality team dispatched. Samples being collected and tested"
      }
    ],
    relatedAccounts: ["4567-8901-WW"]
  },
  {
    id: "OUT-2024-0459",
    reportedDate: "2024-11-13 07:00 AM",
    lastUpdated: "2024-11-13 10:00 AM",
    type: "System Pressure",
    serviceType: "Water",
    severity: "Moderate",
    status: "In Progress",
    affectedArea: "Harrisburg North",
    affectedZipCodes: ["17110", "17112"],
    affectedCustomers: 2100,
    address: "Water Distribution - North Harrisburg Zone",
    description: "Low water pressure reported in the area. Adjusting system valves and pumps.",
    estimatedRestoration: "2024-11-13 01:00 PM",
    timeline: [
      {
        timestamp: "2024-11-13 07:00 AM",
        status: "Reported",
        message: "Low pressure reports received from customers"
      },
      {
        timestamp: "2024-11-13 08:00 AM",
        status: "Investigating",
        message: "System diagnostics underway"
      },
      {
        timestamp: "2024-11-13 10:00 AM",
        status: "In Progress",
        message: "Cause identified. Adjusting pump stations to restore normal pressure"
      }
    ],
    relatedAccounts: ["3456-7890-C"]
  },
  {
    id: "OUT-2024-0455",
    reportedDate: "2024-11-11 03:00 PM",
    lastUpdated: "2024-11-11 08:00 PM",
    type: "Emergency Repair",
    serviceType: "Water",
    severity: "Critical",
    status: "Resolved",
    affectedArea: "West Philadelphia",
    affectedZipCodes: ["19104", "19139"],
    affectedCustomers: 3500,
    address: "Market St & 52nd St, Philadelphia, PA",
    description: "Major water main break repaired. Service restored to all customers.",
    estimatedRestoration: "2024-11-11 08:00 PM",
    timeline: [
      {
        timestamp: "2024-11-11 03:00 PM",
        status: "Reported",
        message: "Major water main break reported"
      },
      {
        timestamp: "2024-11-11 03:30 PM",
        status: "Investigating",
        message: "Emergency crews dispatched"
      },
      {
        timestamp: "2024-11-11 04:15 PM",
        status: "In Progress",
        message: "Water shut off. Excavation and repair in progress"
      },
      {
        timestamp: "2024-11-11 08:00 PM",
        status: "Resolved",
        message: "Repair completed. Water service fully restored"
      }
    ],
    relatedAccounts: []
  }
]
```

### Status Card Design

Each outage should display as a card with:
- **Header:** Outage ID, Type badge, Severity indicator
- **Status Bar:** Visual progress indicator (Reported → Investigating → In Progress → Resolved)
- **Key Info:** Affected area, customer count, service type
- **Description:** Brief explanation of the issue
- **Timeline:** Expandable accordion with detailed status updates
- **ETA:** Prominent display of estimated restoration time
- **Actions:** "Get Updates" button (subscribe to notifications), "View on Map" button

### Visual Design Suggestions
- Use status-specific color coding:
  - **Reported:** Gray/Blue
  - **Investigating:** Yellow
  - **In Progress:** Orange
  - **Resolved:** Green
- Severity badges: Red (Critical), Orange (Moderate), Yellow (Minor)
- Interactive map with zoom and pan capabilities
- Real-time auto-refresh (every 2 minutes) with visual indicator
- Push notification bell icon with unread count
- Mobile-optimized cards that stack vertically
- Loading states with pulse animations
- Empty state: "No active outages in your area" with checkmark icon

---

## Implementation Requirements

### Page-Level Requirements
1. Add "Transactions & Outages" to the main navigation menu (top level)
2. Create route `/transactions-outages` with two-section layout
3. Implement tab navigation or split-panel view for the two sections
4. Ensure all data is responsive and mobile-friendly
5. Add loading states for all API calls
6. Implement error handling with user-friendly messages
7. Add empty states for when no data is available

### Bulk Transactions Section
1. Implement sortable, filterable data table
2. Add date range picker with preset options
3. Create export functionality (CSV and PDF)
4. Display summary cards with real-time calculations
5. Implement pagination
6. Add search functionality across all transaction fields
7. Link transactions to their respective account detail pages
8. Show confirmation numbers as copyable text (click to copy)

### Outages Section
1. Implement interactive Pennsylvania map with clickable regions
2. Create auto-refreshing outage list (every 2 minutes)
3. Add expandable timeline for each outage
4. Implement status filtering and search
5. Create notification subscription modal
6. Add "My Area" quick filter based on customer's registered addresses
7. Highlight outages affecting customer's accounts
8. Include "Report an Issue" call-to-action button

### Data Integration
1. Mock data should align with existing account structure in the app
2. Use consistent account numbers (format: ####-####-X where X is W for water, WW for water & wastewater, C for commercial)
3. Reference the same addresses used elsewhere in the application
4. Ensure transaction amounts reflect realistic Pennsylvania American Water billing
5. Use actual Pennsylvania cities and zip codes
6. Maintain consistency with existing service types (Water, Wastewater)

### Accessibility Requirements
1. Implement ARIA labels for all interactive elements
2. Ensure keyboard navigation works for all features
3. Add screen reader support for dynamic content updates
4. Use semantic HTML throughout
5. Ensure color contrast meets WCAG 2.1 AA standards
6. Add alt text for all icons and visual indicators
7. Implement focus management for modals and expandable sections

### Performance Requirements
1. Lazy load transaction data (paginated)
2. Implement virtual scrolling for large datasets
3. Optimize map rendering
4. Cache outage data with 2-minute refresh interval
5. Use skeleton loaders for better perceived performance
6. Compress exported CSV/PDF files

### Mobile Responsiveness
1. Convert data tables to card layouts on mobile
2. Make filters collapsible/expandable on small screens
3. Ensure map is touch-friendly with pinch-to-zoom
4. Stack sections vertically on mobile
5. Use bottom sheets for filters and actions
6. Optimize touch targets (minimum 44x44px)

---

## SEO & Meta Information

### Page Title
Transactions & Outages - Monitor Your Account Activity | Pennsylvania American Water

### Meta Description
View your bulk transaction history and monitor real-time service outages for Pennsylvania American Water. Track payments, see outage status, and get restoration updates.

### SEO Keywords
- Pennsylvania American Water transactions
- Water bill payment history
- Service outage tracker
- Water main break status
- Planned maintenance schedule
- Real-time outage updates
- Pennsylvania water service alerts
- Account transaction history
- Bulk payment view

---

## Call-to-Action Buttons

### Transactions Section
1. Primary: "Export Transactions" (CSV/PDF options)
2. Secondary: "View Account Details" (links to specific account)
3. Tertiary: "Set Up Auto-Pay"

### Outages Section
1. Primary: "Get Outage Alerts" (subscribe to notifications)
2. Secondary: "Report an Issue" (opens report form)
3. Tertiary: "View Outage History"

---

## Additional Features to Consider

### Notifications & Alerts
- Browser push notifications for outages affecting customer's area
- Email digest option (daily summary of transactions and outages)
- SMS alerts for critical outages
- In-app notification center with unread count

### Analytics & Insights
- **Transaction Trends:** Chart showing spending over time
- **Payment Analytics:** Average monthly cost, payment patterns
- **Outage Statistics:** Historical outage frequency in customer's area

### Integration Points
- Link to payment portal from transaction details
- Link to customer service from outage cards
- Link to account management from transaction filters
- Cross-reference H2O Help to Others Program for eligible credits

### Future Enhancements
- Download transaction receipts (PDF)
- Schedule transaction reports (monthly email)
- Compare transactions across multiple billing periods
- Predictive outage alerts based on weather conditions
- Estimated bill impact from service disruptions

---

## Technical Notes

### State Management
- Use global state for user's accounts list
- Cache transaction data with appropriate TTL
- Implement optimistic updates for filter changes
- Store user's notification preferences

### API Endpoints (Mock Structure)
```
GET /api/transactions?accountId={id}&startDate={date}&endDate={date}&type={type}
GET /api/outages?status={status}&serviceType={type}&region={region}
GET /api/outages/{id}/timeline
POST /api/notifications/subscribe
GET /api/accounts (to populate account filters)
```

### Error Handling
- Network errors: Show retry option
- No data: Display helpful empty state
- API timeout: Show cached data with warning
- Invalid filters: Reset to defaults with message

---

**Note:** Ensure all content follows Pennsylvania American Water's brand guidelines, maintains consistency with existing pages, and provides a seamless user experience across all devices. The feature should integrate naturally with the current navigation structure and design system.
