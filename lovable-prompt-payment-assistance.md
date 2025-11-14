# Payment Assistance Wizards - Pennsylvania American Water

## 1. Installment Plan Application

**Purpose:** Help customers spread past due balance payments over time (free service)

### Eligibility Check Screen
- Display message: "Installment plans are available for customers with past due balances"
- Show customer's current balance status
- Continue button

### Application Form

**Step 1: Account Information**
- Account Number (dropdown - customer's accounts)
- Current Balance Due (display only, auto-filled)
- Past Due Amount (display only, auto-filled)

**Step 2: Payment Plan Preferences**
- Desired Monthly Payment Amount (input field with $ - minimum $25)
- Preferred Payment Date (dropdown):
  - 1st of month
  - 15th of month
  - Same as original due date
- Payment Method (dropdown):
  - Auto-Pay (Bank Account)
  - Auto-Pay (Credit/Debit Card)
  - Manual Payment Each Month

**Step 3: Contact Information**
- Phone Number (pre-filled, editable)
- Email (pre-filled, editable)
- Best Time to Call (dropdown): Morning/Afternoon/Evening

**Step 4: Agreement**
- Checkbox: "I understand I must make all scheduled payments on time"
- Checkbox: "I understand I must keep my current bills paid while on this plan"
- Submit button: "Request Installment Plan"

**Confirmation:**
- Show request number
- Message: "We'll review your request and contact you within 2 business days to finalize your payment plan"
- Display proposed payment schedule based on amount entered

---

## 2. One-Time Payment Extension

**Purpose:** Extend the current bill due date (available once per year)

### Eligibility Check Screen
- Show current due date
- Check if extension already used this year (display message if yes)
- Continue button

### Application Form

**Step 1: Account Information**
- Account Number (dropdown - customer's accounts)
- Current Due Date (display only)
- Amount Due (display only)

**Step 2: Extension Request**
- Reason for Extension (dropdown):
  - Temporary Financial Hardship
  - Delayed Income/Paycheck
  - Unexpected Expense
  - Other
- Requested New Due Date (date picker - up to 30 days from original date)
- Additional Comments (text area, optional)

**Step 3: Contact Information**
- Phone Number (pre-filled, editable)
- Email (pre-filled, editable)

**Step 4: Agreement**
- Checkbox: "I understand this is a one-time courtesy extension per year"
- Checkbox: "I agree to pay the full amount by the new due date"
- Submit button: "Request Extension"

**Confirmation:**
- Show request number
- Message: "Extension request submitted. You'll receive confirmation within 24 hours"
- Display original and requested new due dates

---

## 3. Medical Hardship Assistance

**Purpose:** Postpone service termination for 30 days due to medical emergency in household

### Important Notice Screen
- Display: "If someone in your household has a serious medical condition that requires water service, you may qualify for a 30-day postponement"
- Requirements:
  - Licensed physician, physician assistant, or nurse practitioner must complete certification
  - Current month's bill must be paid during the 30-day period
  - Provides time to make payment arrangements for past due amounts
- Continue button

### Application Form

**Step 1: Account Information**
- Account Number (dropdown - customer's accounts)
- Service Address (display only)
- Current Balance (display only)

**Step 2: Medical Information**
- Patient Name (text input)
- Relationship to Account Holder (dropdown):
  - Self
  - Spouse/Partner
  - Child
  - Parent
  - Other Household Member
- Medical Condition Affects (checkboxes):
  - Personal Hygiene Needs
  - Medical Equipment/Dialysis
  - Medication Requirements
  - Other Critical Health Need
- Brief Description (text area - "How would loss of water service impact this condition?")

**Step 3: Healthcare Provider Information**
- Provider Name (text input - "Physician, PA, or Nurse Practitioner")
- Medical Practice/Hospital (text input)
- Provider Phone Number (input)
- Provider Fax Number (input, optional)

**Step 4: Certification Upload**
- Radio button options:
  - "I have a completed medical certificate to upload now"
  - "Please fax the certificate to my healthcare provider to complete"
- If Upload Selected: File upload (PDF, JPG, PNG)
- If Fax Selected: "We'll fax the certificate to the provider number you entered above"

**Step 5: Contact Information**
- Your Phone Number (pre-filled, editable)
- Your Email (pre-filled, editable)
- Best Time to Call (dropdown)

**Step 6: Acknowledgment**
- Checkbox: "I understand service termination will be postponed for 30 days"
- Checkbox: "I understand I must pay the current month's bill during this period"
- Checkbox: "I certify the information provided is accurate"
- Submit button: "Submit Medical Hardship Application"

**Confirmation:**
- Show application number
- If certificate uploaded: "Application submitted. You'll receive confirmation within 24 hours"
- If fax requested: "Certificate will be faxed to your healthcare provider within 2 hours. Application will be processed once we receive the completed form"
- Display important reminder: "Continue to pay current charges while application is reviewed"

---

## Common Features for All Wizards

**Navigation:**
- Accessible from main menu under "Payment Assistance Programs"
- Breadcrumb navigation showing current step
- Back button on each step (except final confirmation)
- Save and exit option (returns to dashboard)

**Validation:**
- Real-time field validation
- Clear error messages
- Required fields marked with *
- Progress indicator showing steps

**Accessibility:**
- WCAG 2.1 AA compliant
- Keyboard navigation
- Screen reader compatible
- Mobile responsive design

**After Submission:**
- Email confirmation with request/application number
- Copy sent to customer's email
- Printable summary page
- Link to check status in MyWater account
