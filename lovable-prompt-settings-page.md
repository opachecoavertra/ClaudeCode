# Settings Page - Pennsylvania American Water

## Overview
Centralized settings page where residential customers can manage account preferences, notifications, billing, security, and communication options.

**Menu Location:** Main Menu > Settings (gear icon) OR User Profile dropdown > Settings

---

## Settings Page Layout

### Page Header
- Title: "Settings"
- User name and account info
- Last updated: [timestamp]

### Left Navigation (Desktop) / Tabs (Mobile)
- Account Preferences
- Notifications
- Billing & Payments
- Communication
- Security & Privacy
- Water Usage Alerts
- Program Enrollments
- Accessibility

---

## 1. Account Preferences

### Default Account
- If user has multiple accounts:
  - Dropdown to select default account
  - Display on login checkbox
  - "This account will be shown first when you log in"

### Language
- Language selection (dropdown):
  - English
  - Spanish
  - Other languages as available
- "Apply to all communications" checkbox

### Time Zone
- Auto-detected (display)
- Manual override option (dropdown)

### Date/Time Format
- Date format (dropdown):
  - MM/DD/YYYY
  - DD/MM/YYYY
  - YYYY-MM-DD
- Time format (radio buttons):
  - 12-hour (AM/PM)
  - 24-hour

### Dashboard Preferences
- Show quick stats on dashboard (toggle)
- Show recent transactions (toggle)
- Show upcoming service orders (toggle)
- Show usage chart (toggle)
- Default view (dropdown):
  - Overview
  - Billing
  - Usage
  - Service Orders

**Save Changes Button**

---

## 2. Notifications

### Email Notifications
**Account & Billing:**
- ☑ Bill ready notification
- ☑ Payment received confirmation
- ☑ Payment due reminder (select: 3, 5, 7 days before)
- ☑ Auto-pay confirmation
- ☑ Failed payment alert
- ☐ Budget billing updates

**Service & Orders:**
- ☑ Service order confirmation
- ☑ Service order updates
- ☑ Technician en route notification
- ☑ Service completion notification
- ☐ Scheduled maintenance notices

**Water Quality & Outages:**
- ☑ Outage alerts (in my area)
- ☑ Water quality alerts
- ☑ Planned maintenance notifications
- ☑ Boil water advisories
- ☐ System pressure alerts

**Account Activity:**
- ☑ Password changed
- ☑ Profile updated
- ☑ New authorized user added
- ☐ Login from new device

**Feedback & Forms:**
- ☑ Submission confirmation
- ☑ Response received
- ☑ Status updates
- ☐ Survey invitations

**Marketing & Promotions:**
- ☐ Water saving tips
- ☐ Conservation programs
- ☐ Community events
- ☐ Newsletter

### SMS/Text Notifications
**Phone Number for SMS:** [input field with validation]
- ☑ Bill due reminders
- ☑ Payment confirmations
- ☑ Outage alerts
- ☑ Service appointment reminders
- ☑ Technician arrival notifications
- ☐ High usage alerts
- ☐ Emergency alerts only

**SMS Frequency:**
- Radio buttons:
  - All notifications
  - Important only (bills, outages, emergencies)
  - Emergency only

### Push Notifications (if using mobile app)
- ☑ Enable push notifications
- ☑ Service updates
- ☑ Bill reminders
- ☑ Outage alerts
- ☐ Usage alerts
- ☐ Promotional

### Notification Delivery Times
- Preferred notification hours:
  - Start time: [dropdown] 8:00 AM
  - End time: [dropdown] 9:00 PM
- "Do not send notifications outside these hours (emergencies excepted)"

**Email Address:** [display/edit]
**Verify email button** (if changed)

**Save Notification Preferences Button**

---

## 3. Billing & Payments

### Paperless Billing
- Toggle: Enroll in paperless billing
- "Receive bills via email instead of mail"
- Current status: Enrolled / Not Enrolled
- Date enrolled: [if applicable]
- Savings: "Save trees and $2/month on your bill"

### Auto-Pay Settings
**Status:** Enabled / Disabled (toggle)

**If Enabled, show:**
- Payment method: [Bank Account ending in 1234] [Edit]
- Payment date: [5 days before due date] [Change]
- Backup payment method: [Add/Edit]
- Auto-pay amount:
  - Radio: Full balance
  - Radio: Fixed amount: $____ [input]
- Email confirmation: Yes [toggle]
- Started on: [date]

**If Disabled:**
- "Set up automatic payments" button
- Benefits listed:
  - Never miss a payment
  - No late fees
  - Convenient and secure

### Payment Methods
**Saved Payment Methods:**

**Card 1:**
- Visa ending in 4567
- Expires: 12/2025
- Default: Yes
- [Edit] [Remove] buttons

**Card 2:**
- Bank Account ending in 1234
- Routing: ***456
- [Edit] [Remove] buttons

**[Add New Payment Method] button**

### Add/Edit Payment Method Modal
- Payment type (radio):
  - Credit/Debit Card
  - Bank Account (ACH)
- Card number / Account number
- Expiration / Routing number
- Security code / Account type (Checking/Savings)
- Billing zip code
- Nickname (optional) "e.g., Primary Checking"
- Set as default (checkbox)
- [Save] [Cancel]

### Budget Billing
- Current status: Enrolled / Not Enrolled
- If enrolled:
  - Current monthly amount: $85
  - Next review date: [date]
  - [Manage Budget Billing] button
- If not enrolled:
  - "Smooth out seasonal billing variations"
  - [Enroll in Budget Billing] button

### Payment Reminders
- Days before due date (dropdown): 3, 5, 7, 10 days
- Reminder method:
  - ☑ Email
  - ☑ SMS
  - ☐ Push notification

### Billing Address
- Same as service address (checkbox)
- If different:
  - Street Address
  - City, State, ZIP
  - [Update Address] button

**Save Billing Settings Button**

---

## 4. Communication Preferences

### Contact Information
**Primary Phone:** [input]
- Type: Mobile / Home / Work
**Secondary Phone:** [input] (optional)
- Type: Mobile / Home / Work
**Email:** [input]
- [Verify Email] button if changed

### Preferred Contact Method
- Radio buttons:
  - Email (fastest response)
  - Phone
  - SMS/Text
  - No preference

### Best Time to Contact
- Checkboxes:
  - ☑ Morning (8 AM - 12 PM)
  - ☑ Afternoon (12 PM - 5 PM)
  - ☐ Evening (5 PM - 9 PM)

### Do Not Contact Preferences
- ☐ Do not call (except for emergencies)
- ☐ Do not send promotional emails
- ☐ Do not send physical mail (except bills/legal notices)

### Service Address Access Instructions
**For Technician Visits:**
- Gate code / Access code: [input] (optional)
- Parking instructions: [text area]
- Special access notes: [text area]
  - e.g., "Meter in basement, use side entrance"
  - "Dog in backyard, please call before entering"

### Communication Language
- Dropdown: English / Spanish / Other

**Save Communication Preferences Button**

---

## 5. Security & Privacy

### Password & Security

**Change Password:**
- Current password: [input - password]
- New password: [input - password]
  - Password strength indicator
  - Requirements shown:
    - At least 8 characters
    - One uppercase letter
    - One number
    - One special character
- Confirm new password: [input - password]
- [Change Password] button

**Security Questions:**
- Question 1: [dropdown]
- Answer: [input]
- Question 2: [dropdown]
- Answer: [input]
- [Update Security Questions] button

**Two-Factor Authentication (2FA):**
- Status: Enabled / Disabled (toggle)
- If enabled:
  - Method: SMS to ***-***-1234 [Change]
  - Backup codes: [View/Download]
  - Trusted devices: [Manage]
- If disabled:
  - "Add extra security to your account"
  - [Enable 2FA] button

### Account Access

**Authorized Users:**
- List of users who have access to this account:

**User 1:**
- Name: Jane Doe (You - Primary)
- Email: jane@example.com
- Access level: Full
- Status: Active

**User 2:**
- Name: John Doe
- Email: john@example.com
- Access level: View Only
- Added: 01/15/2024
- [Edit] [Remove]

**[Add Authorized User] button**
- "Allow family members to view bills or make payments"

**Add User Modal:**
- First Name, Last Name
- Email address
- Phone (optional)
- Access level (dropdown):
  - View Only (see bills and usage)
  - Payment Only (view and pay bills)
  - Full Access (all features except delete account)
- Send invitation email (checkbox)
- [Send Invitation] [Cancel]

### Login Activity
**Recent Logins:**
- Table showing:
  - Date/Time
  - Device/Browser
  - Location (IP-based)
  - Status (Success/Failed)

Example:
- 11/17/2025 9:30 AM | Chrome on Windows | Pittsburgh, PA | Success
- 11/16/2025 7:15 PM | Safari on iPhone | Pittsburgh, PA | Success
- 11/15/2025 2:20 PM | Chrome on Windows | Pittsburgh, PA | Success

**[View Full History] button** (last 90 days)
**"Don't recognize a login? [Change your password]"**

### Privacy Settings

**Data Sharing:**
- ☐ Share usage data for conservation research (anonymous)
- ☐ Share data with energy/water saving programs
- ☑ Allow American Water to contact me about programs I may qualify for

**Account Visibility:**
- ☐ Show my address in neighborhood comparison reports (anonymous)
- ☐ Participate in community usage benchmarking

**Marketing Preferences:**
- ☐ Email promotions and tips
- ☐ Partner offers (water-saving products, etc.)
- ☐ Surveys and feedback requests

**Download My Data:**
- "Request a copy of all your account data"
- [Request Data Export] button
- Format: PDF or CSV
- Delivered via email within 30 days

**Delete Account:**
- "Permanently delete my online account"
- Note: "This does not close your water service account"
- [Request Account Deletion] button

**Save Privacy Settings Button**

---

## 6. Water Usage Alerts

### High Usage Alerts
- Toggle: Enable high usage alerts
- Alert threshold:
  - Radio: Automatic (we'll detect unusual spikes)
  - Radio: Custom: Alert when daily usage exceeds [input] gallons
- Delivery method:
  - ☑ Email
  - ☑ SMS
  - ☐ Push notification
- Alert frequency:
  - Dropdown: Immediate / Daily summary / Weekly summary

### Leak Detection Alerts
- Toggle: Enable leak detection notifications
- "We'll alert you if we detect continuous water flow that may indicate a leak"
- Sensitivity:
  - Radio: High (more frequent alerts)
  - Radio: Medium (balanced)
  - Radio: Low (only significant leaks)
- Delivery method:
  - ☑ Email
  - ☑ SMS
  - ☐ Push notification

### Conservation Goals
- Toggle: Set water conservation goals
- Monthly goal: [input] gallons (suggested: 3,000 based on household)
- Compare to:
  - ☑ Similar homes in my area
  - ☑ My historical usage
  - ☑ State average
- Progress notifications:
  - ☐ Weekly progress updates
  - ☑ Monthly summary
  - ☑ Alert if goal exceeded

### Usage Report Frequency
- Weekly usage report (toggle)
- Monthly usage report (toggle)
- Include comparison data (toggle)
- Delivery method: Email / SMS / Both

**Save Usage Alert Settings Button**

---

## 7. Program Enrollments

### Current Enrollments
**Display cards for each program customer is enrolled in:**

**H2O Help to Others - Bill Discount:**
- Status: Active
- Discount level: 30%
- Enrolled since: 03/15/2024
- Next verification: 03/15/2025
- [View Details] [Update Information]

**Budget Billing:**
- Status: Active
- Monthly amount: $85
- Next review: 12/01/2025
- [Manage] button

**Paperless Billing:**
- Status: Active
- Savings: $24/year
- [Manage] button

### Available Programs
**Programs you may qualify for:**

**H2O Help to Others Grant:**
- Up to $500/year assistance
- [Check Eligibility] [Apply]

**Medical Hardship Assistance:**
- 30-day service postponement
- [Learn More] [Apply]

**Installment Plan:**
- Spread past due balance over time
- [Check Eligibility] [Apply]

**Water Saving Kit:**
- Free kit with conservation tools
- [Request Kit]

**Arrearage Forgiveness:**
- Forgive past due balances
- [Check Eligibility] [Learn More]

### Program Notifications
- ☑ Notify me about new assistance programs
- ☑ Remind me to renew program enrollments
- ☑ Alert me about program deadlines

**Save Program Preferences Button**

---

## 8. Accessibility

### Display Settings
**Text Size:**
- Radio buttons:
  - Small
  - Medium (default)
  - Large
  - Extra Large
- Live preview shown

**Contrast Mode:**
- Toggle: High contrast mode
- "Improves readability for low vision users"

**Color Scheme:**
- Radio buttons:
  - Light (default)
  - Dark
  - System (follow device settings)

### Assistive Features
**Screen Reader Optimization:**
- Toggle: Enable enhanced screen reader support
- "Provides additional context for screen readers"

**Keyboard Navigation:**
- Toggle: Enhanced keyboard navigation
- "Shows visible focus indicators"
- "Enables keyboard shortcuts"

**Reduce Motion:**
- Toggle: Reduce animations
- "Minimizes motion for users with vestibular disorders"

### Reading Assistance
**Dyslexia-Friendly Font:**
- Toggle: Use dyslexia-friendly font
- Changes to OpenDyslexic font

**Reading Guide:**
- Toggle: Show reading guide
- "Highlights current line when reading"

### Language & Translation
**Interface Language:** [Dropdown]
**Enable Auto-Translate:** Toggle
- "Automatically translate content"

### Alternative Formats
**Bill Format Preference:**
- Radio buttons:
  - Standard PDF
  - Large print PDF
  - Screen-reader optimized HTML
  - Braille (request by mail)

**Document Delivery:**
- ☑ Email (default)
- ☐ Mail (large print)
- ☐ Phone (automated reading)

### Accessibility Help
- "Need assistance with accessibility features?"
- [Contact Accessibility Support] button
- Phone: 1-800-XXX-XXXX (TTY available)
- Email: accessibility@amwater.com

**Save Accessibility Settings Button**

---

## Global Features (All Settings Pages)

### Save Behavior
- "Save Changes" button at bottom of each section
- "You have unsaved changes" warning if navigating away
- Success message: "Settings saved successfully"
- Timestamp shown: "Last updated: [date/time]"

### Reset Options
- "Reset to Defaults" button (with confirmation)
- Only resets current section, not all settings

### Mobile Responsive
- Tabs instead of left navigation
- Collapsible sections
- Bottom sticky save button
- Swipe between sections

### Search Settings
- Search bar at top
- Search across all settings
- Highlights matching settings
- Quick jump to section

### Help & Tooltips
- (i) icons next to complex settings
- Hover/tap for explanations
- Links to help articles
- "Need help?" floating button

---

## UI Design (Following App System Design)

### Layout
- Clean, organized sections with clear headers
- Card-based design for grouped settings
- Toggle switches for enable/disable options
- Radio buttons for single-choice
- Checkboxes for multi-choice
- Consistent spacing and padding

### Colors
- Primary action buttons: Blue (#2196F3)
- Success messages: Green (#4CAF50)
- Warning messages: Orange (#FF9800)
- Destructive actions: Red (#F44336)
- Disabled items: Gray (#9E9E9E)

### Typography
- Section headers: 24px, bold
- Subsection headers: 18px, semibold
- Body text: 16px, regular
- Helper text: 14px, gray

### Interactive Elements
- Toggle switches with smooth animation
- Input fields with clear focus states
- Button hover/active states
- Loading indicators on save
- Success checkmark animations

---

## Technical Considerations

### API Endpoints (suggested)
```
GET /api/settings/account
PUT /api/settings/account
GET /api/settings/notifications
PUT /api/settings/notifications
GET /api/settings/billing
PUT /api/settings/billing
POST /api/settings/payment-methods
DELETE /api/settings/payment-methods/{id}
GET /api/settings/security
PUT /api/settings/security/password
POST /api/settings/security/2fa
GET /api/settings/authorized-users
POST /api/settings/authorized-users
GET /api/settings/usage-alerts
PUT /api/settings/usage-alerts
GET /api/settings/accessibility
PUT /api/settings/accessibility
```

### Security
- Require current password for sensitive changes
- Email verification for email changes
- 2FA prompt for security setting changes
- Session timeout after inactivity
- Audit log of all setting changes

### Performance
- Save settings per section (not all at once)
- Optimistic UI updates
- Background save without full page reload
- Cache settings locally
- Sync across devices

### Validation
- Real-time validation on inputs
- Clear error messages
- Prevent invalid data submission
- Format phone numbers automatically
- Verify email format
- Check password strength
