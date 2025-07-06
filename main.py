from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import os
import time
from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
def detect_recaptcha_verification_screen(driver):
    """
    Detects if the Facebook reCAPTCHA verification screen is currently displayed.
    
    Args:
        driver: Selenium WebDriver instance
        
    Returns:
        bool: True if reCAPTCHA verification screen is detected, False otherwise
    """
    try:
        # Method 1: Check for the specific heading text "Help us confirm that it's you"
        try:
            heading_element = driver.find_element("xpath", "//*[contains(text(), 'Help us confirm that it')]")
            if heading_element.is_displayed():
                print("reCAPTCHA verification screen detected via heading text")
                return True
        except:
            pass
        
        # Method 2: Check for reCAPTCHA iframe
        try:
            recaptcha_iframe = driver.find_element("css selector", "iframe[id*='captcha']")
            if recaptcha_iframe.is_displayed():
                print("reCAPTCHA verification screen detected via iframe")
                return True
        except:
            pass
        
        # Method 3: Check for reCAPTCHA iframe with specific ID
        try:
            recaptcha_iframe = driver.find_element("id", "captcha-recaptcha")
            if recaptcha_iframe.is_displayed():
                print("reCAPTCHA verification screen detected via captcha-recaptcha iframe")
                return True
        except:
            pass
        
        # Method 4: Check for Continue button with aria-disabled="true"
        try:
            continue_button = driver.find_element("css selector", "div[aria-disabled='true'][aria-label='Continue']")
            if continue_button.is_displayed():
                print("reCAPTCHA verification screen detected via disabled Continue button")
                return True
        except:
            pass
        
        # Method 5: Check for the specific combination of elements
        try:
            page_source = driver.page_source
            if ("Help us confirm that it's you" in page_source and 
                "captcha" in page_source.lower() and 
                "Continue" in page_source):
                print("reCAPTCHA verification screen detected via page source analysis")
                return True
        except:
            pass
        
        # Method 6: Check for referer_frame.php which is specific to Facebook's reCAPTCHA
        try:
            referer_frame = driver.find_element("css selector", "iframe[src*='referer_frame.php']")
            if referer_frame.is_displayed():
                print("reCAPTCHA verification screen detected via referer_frame")
                return True
        except:
            pass
        
        print("reCAPTCHA verification screen not detected")
        return False
        
    except Exception as e:
        print(f"Error detecting reCAPTCHA verification screen: {e}")
        return False
def detect_identity_verification_screen(driver):
    """
    Detects if the Facebook identity verification screen is currently displayed.
    
    Args:
        driver: Selenium WebDriver instance
        
    Returns:
        bool: True if identity verification screen is detected, False otherwise
    """
    try:
        # Method 1: Check for the specific heading text
        heading_selectors = [
            "span[dir='auto']:contains('Confirm your identity with a video selfie')",
            "//*[contains(text(), 'Confirm your identity with a video selfie')]",
            "span:contains('Confirm your identity with a video selfie')"
        ]
        
        # Method 2: Check for the description text
        description_text = "To make sure that you're a real person, we need you to record a video selfie"
        
        # Method 3: Check for Continue button with specific classes
        continue_button_selector = "div[aria-label='Continue'][role='button']"
        
        # Method 4: Check for the combination of specific class patterns
        main_container_selector = "div[class*='x6s0dn4'][role='main']"
        
        # Try different approaches to detect the screen
        
        # Approach 1: Look for the main heading text
        try:
            heading_element = driver.find_element("xpath", "//*[contains(text(), 'Confirm your identity with a video selfie')]")
            if heading_element.is_displayed():
                print("Identity verification screen detected via heading text")
                return True
        except:
            pass
        
        # Approach 2: Look for the description text
        try:
            description_element = driver.find_element("xpath", f"//*[contains(text(), '{description_text}')]")
            if description_element.is_displayed():
                print("Identity verification screen detected via description text")
                return True
        except:
            pass
        
        # Approach 3: Look for Continue button with aria-label
        try:
            continue_button = driver.find_element("css selector", continue_button_selector)
            if continue_button.is_displayed():
                # Also check if we can find the heading nearby
                try:
                    driver.find_element("xpath", "//*[contains(text(), 'Confirm your identity')]")
                    print("Identity verification screen detected via Continue button + heading")
                    return True
                except:
                    pass
        except:
            pass
        
        # Approach 4: Look for the specific combination of elements
        try:
            # Check for main container
            main_container = driver.find_element("css selector", main_container_selector)
            if main_container.is_displayed():
                # Check if it contains both the heading and description
                page_source = driver.page_source
                if ("Confirm your identity with a video selfie" in page_source and 
                    "video selfie" in page_source and 
                    "Continue" in page_source):
                    print("Identity verification screen detected via page source analysis")
                    return True
        except:
            pass
        
        # Approach 5: Check for specific class combinations that are unique to this screen
        try:
            # Look for the specific nested div structure with video selfie context
            elements = driver.find_elements("css selector", "div.x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x2lah0s.x193iq5w.x1cnzs8.xx6bls6")
            for element in elements:
                if element.is_displayed() and "video selfie" in element.text:
                    print("Identity verification screen detected via specific class structure")
                    return True
        except:
            pass
        
        print("Identity verification screen not detected")
        return False
        
    except Exception as e:
        print(f"Error detecting identity verification screen: {e}")
        return False


# Alternative simpler version focusing on key text elements
def detect_identity_verification_simple(driver):
    """
    Simplified version that focuses on key text elements.
    
    Args:
        driver: Selenium WebDriver instance
        
    Returns:
        bool: True if identity verification screen is detected, False otherwise
    """
    try:
        # Get page source and check for key phrases
        page_source = driver.page_source.lower()
        
        # Key indicators of the identity verification screen
        key_phrases = [
            "confirm your identity with a video selfie",
            "record a video selfie",
            "move your head during the recording"
        ]
        
        # Check if at least 2 of the key phrases are present
        phrase_count = sum(1 for phrase in key_phrases if phrase in page_source)
        
        if phrase_count >= 2:
            print("Identity verification screen detected via text analysis")
            return True
        
        return False
        
    except Exception as e:
        print(f"Error in simple detection: {e}")
        return False

def append_to_csv(filename, data_dict, fieldnames):
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data_dict)


def get_profile_name(driver):
    """
    Extracts profile name from current Facebook page using multiple methods.
    
    Args:
        driver: Selenium WebDriver instance
    
    Returns:
        str: Profile name or None if not found
    """
    try:
        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Method 1: CSS Selector - h1 with html-h1 class
        try:
            name_element = driver.find_element(By.CSS_SELECTOR, "h1.html-h1")
            name = name_element.text.strip()
            if name:
                return ' '.join(name.split())
        except NoSuchElementException:
            pass
        
        # Method 2: CSS Selector - any h1 with class containing 'html-h1'
        try:
            name_element = driver.find_element(By.CSS_SELECTOR, "h1[class*='html-h1']")
            name = name_element.text.strip()
            if name:
                return ' '.join(name.split())
        except NoSuchElementException:
            pass
        
        # Method 3: XPath - h1 with html-h1 class
        try:
            name_element = driver.find_element(By.XPATH, "//h1[contains(@class, 'html-h1')]")
            name = name_element.text.strip()
            if name:
                return ' '.join(name.split())
        except NoSuchElementException:
            pass
        
        # Method 4: CSS Selector - span containing h1
        try:
            name_element = driver.find_element(By.CSS_SELECTOR, "span h1")
            name = name_element.text.strip()
            if name:
                return ' '.join(name.split())
        except NoSuchElementException:
            pass
        
        # Method 5: XPath - any h1 tag (less specific)
        try:
            name_element = driver.find_element(By.XPATH, "//h1")
            name = name_element.text.strip()
            if name:
                return ' '.join(name.split())
        except NoSuchElementException:
            pass
        
        # Method 6: CSS Selector - look for strong tags in the profile area
        try:
            name_elements = driver.find_elements(By.CSS_SELECTOR, "strong")
            for element in name_elements:
                text = element.text.strip()
                # Skip if it's just numbers (likes, followers)
                if text and not text.isdigit() and len(text) > 2:
                    return ' '.join(text.split())
        except NoSuchElementException:
            pass
        
        # Method 7: XPath - look for text in div containing profile info
        try:
            profile_divs = driver.find_elements(By.XPATH, "//div[contains(@class, 'x78zum5')]//h1")
            for div in profile_divs:
                text = div.text.strip()
                if text and len(text) > 2:
                    return ' '.join(text.split())
        except NoSuchElementException:
            pass
        
        # Method 8: Look for aria-label or title attributes
        try:
            elements = driver.find_elements(By.XPATH, "//*[@aria-label or @title]")
            for element in elements:
                aria_label = element.get_attribute('aria-label')
                title = element.get_attribute('title')
                
                if aria_label and len(aria_label) > 2 and not aria_label.isdigit():
                    return ' '.join(aria_label.split())
                if title and len(title) > 2 and not title.isdigit():
                    return ' '.join(title.split())
        except NoSuchElementException:
            pass
        
        # Method 9: Check page title
        try:
            title = driver.title
            if title and "Facebook" in title:
                # Extract name from title (usually format: "Name | Facebook")
                name = title.split("|")[0].strip()
                if name and name != "Facebook":
                    return name
        except:
            pass
        
        # Method 10: Look for meta property og:title
        try:
            meta_element = driver.find_element(By.XPATH, "//meta[@property='og:title']")
            content = meta_element.get_attribute('content')
            if content:
                return content.strip()
        except NoSuchElementException:
            pass
        
        return None
        
    except TimeoutException:
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
  
  
def scrape_contact_and_basic_info(driver):
    """
    Function to click 'Contact and basic info' button and scrape the information
    
    Args:
        driver: Selenium WebDriver instance
    
    Returns:
        dict: Dictionary containing scraped contact and basic info
    """
    
    scraped_data = {
        "profile_name": get_profile_name(driver),
        'contact_info': {},
        'websites_and_social_links': {},
        'basic_info': {},
        'categories': {}
    }
    
    try:
        # Multiple strategies to find and click the contact button
        contact_button = None
        click_successful = False
        
        # Strategy 1: Try by href containing contact_and_basic_info
        try:
            contact_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'contact_and_basic_info')]"))
            )
            print("Found contact button by href")
        except:
            pass
        
        # Strategy 2: Try by text content
        if not contact_button:
            try:
                contact_button = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Contact and basic info')]"))
                )
                print("Found contact button by text")
            except:
                pass
        
        # Strategy 3: Try by span text inside link
        if not contact_button:
            try:
                contact_button = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//a//span[contains(text(), 'Contact and basic info')]/parent::a"))
                )
                print("Found contact button by span text")
            except:
                pass
        
        if not contact_button:
            print("Could not find contact button with any strategy")
            return None
        
        # Multiple click strategies
        try:
            # Strategy 1: Regular click
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(contact_button))
            contact_button.click()
            click_successful = True
            print("Successfully clicked with regular click")
        except ElementClickInterceptedException:
            try:
                # Strategy 2: JavaScript click
                driver.execute_script("arguments[0].click();", contact_button)
                click_successful = True
                print("Successfully clicked with JavaScript")
            except:
                try:
                    # Strategy 3: ActionChains click
                    actions = ActionChains(driver)
                    actions.move_to_element(contact_button).click().perform()
                    click_successful = True
                    print("Successfully clicked with ActionChains")
                except:
                    try:
                        # Strategy 4: Scroll and click
                        driver.execute_script("arguments[0].scrollIntoView(true);", contact_button)
                        time.sleep(1)
                        driver.execute_script("arguments[0].click();", contact_button)
                        click_successful = True
                        print("Successfully clicked after scrolling")
                    except:
                        pass
        
        if not click_successful:
            print("Failed to click contact button with all strategies")
            return None
        
        # Wait for the page to load and content to appear
        time.sleep(3)
        
        # Wait for any of the expected sections to appear
        try:
            WebDriverWait(driver, 10).until(
                EC.any_of(
                    EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Contact info')]")),
                    EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Basic info')]")),
                    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'No contact info')]"))
                )
            )
        except TimeoutException:
            print("Content did not load after clicking")
            return scraped_data  # Return empty data instead of None
        
        # Scrape Contact Info Section
        try:
            # Look for "No contact info to show" message
            no_contact_elements = driver.find_elements(By.XPATH, "//span[contains(text(), 'No contact info to show')]")
            if no_contact_elements:
                scraped_data['contact_info']['status'] = 'No contact info to show'
            else:
                # Try to find actual contact information
                contact_elements = driver.find_elements(By.XPATH, "//h2[contains(text(), 'Contact info')]/following::div//span[contains(@class, 'x193iq5w') and string-length(text()) > 2]")
                if contact_elements:
                    contact_info_list = [elem.text.strip() for elem in contact_elements[:5] if elem.text.strip()]  # Limit to first 5
                    scraped_data['contact_info']['details'] = list(set(contact_info_list))  # Remove duplicates
                else:
                    scraped_data['contact_info']['status'] = 'No contact info found'
        except Exception as e:
            scraped_data['contact_info']['error'] = f'Error scraping contact info: {str(e)}'
        
        # Scrape Websites and Social Links Section
        try:
            no_links_elements = driver.find_elements(By.XPATH, "//span[contains(text(), 'No links to show')]")
            if no_links_elements:
                scraped_data['websites_and_social_links']['status'] = 'No links to show'
            else:
                # Try to find actual links
                link_elements = driver.find_elements(By.XPATH, "//h2[contains(text(), 'Websites and social links')]/following::div//a[@href]")
                if link_elements:
                    links_list = [elem.get_attribute('href') for elem in link_elements if elem.get_attribute('href')]
                    scraped_data['websites_and_social_links']['links'] = links_list
                else:
                    scraped_data['websites_and_social_links']['status'] = 'No links found'
        except Exception as e:
            scraped_data['websites_and_social_links']['error'] = f'Error scraping social links: {str(e)}'
        
        # Scrape Basic Info Section
        try:
            # Look for gender information
            gender_elements = driver.find_elements(By.XPATH, "//span[contains(text(), 'Male') or contains(text(), 'Female') or contains(text(), 'Custom')]")
            if gender_elements:
                scraped_data['basic_info']['gender'] = gender_elements[0].text
            
            # Look for other basic info
            basic_info_elements = driver.find_elements(By.XPATH, "//h2[contains(text(), 'Basic info')]/following::div//span[contains(@class, 'x193iq5w') and string-length(text()) > 1]")
            if basic_info_elements:
                basic_info_list = []
                for elem in basic_info_elements[:10]:  # Limit to first 10
                    text = elem.text.strip()
                    if text and text not in ['Gender', 'Male', 'Female', 'Custom'] and len(text) > 1:
                        basic_info_list.append(text)
                if basic_info_list:
                    scraped_data['basic_info']['additional'] = list(set(basic_info_list))  # Remove duplicates
        except Exception as e:
            scraped_data['basic_info']['error'] = f'Error scraping basic info: {str(e)}'
        
        # Scrape Categories Section
        try:
            category_elements = driver.find_elements(By.XPATH, "//h2[contains(text(), 'Categories')]/following::div//span[contains(@class, 'x193iq5w') and string-length(text()) > 2]")
            if category_elements:
                categories_list = [elem.text.strip() for elem in category_elements[:5] if elem.text.strip()]  # Limit to first 5
                scraped_data['categories']['categories'] = list(set(categories_list))  # Remove duplicates
            else:
                scraped_data['categories']['status'] = 'No categories found'
        except Exception as e:
            scraped_data['categories']['error'] = f'Error scraping categories: {str(e)}'
        
        print("Successfully scraped contact and basic info:")
        for section, data in scraped_data.items():
            print(f"{section}: {data}")
        
        return scraped_data
        
    except Exception as e:
        print(f"Unexpected error occurred while scraping: {str(e)}")
        # Return empty data structure instead of None to prevent NoneType errors
        return {
            'contact_info': {'error': str(e)},
            'websites_and_social_links': {'error': str(e)},
            'basic_info': {'error': str(e)},
            'categories': {'error': str(e)}
        }
        
           
  
    
def scrape_facebook_contact_info(driver, timeout=10):

    
    contact_info = {
        "name": get_profile_name(driver),
        'address': None,
        'phone_numbers': [],
        'emails': [],
        'map_coordinates': None,
        'website': None
    }
    
    try:
        # Wait for page to load
        time.sleep(2)
        
        # Try to find "Contact info" section specifically
        contact_section = None
        
        # Method 1: Look for "Contact info" heading
        try:
            contact_headings = driver.find_elements(By.XPATH, "//*[contains(text(), 'Contact info') or contains(text(), 'Contact Info')]")
            if contact_headings:
                # Find the parent container that holds all contact info
                for heading in contact_headings:
                    try:
                        # Go up to find the main container
                        contact_section = heading.find_element(By.XPATH, "./ancestor::div[contains(@class, 'x1hq5gj4') or contains(@class, 'xx6bls6')][1]")
                        if contact_section:
                            break
                    except:
                        continue
        except Exception as e:
            print(f"Method 1 failed: {e}")
        
        # Method 2: Look for elements with contact-related icons/images
        if not contact_section:
            try:
                # Look for phone, email, or location icons
                icon_elements = driver.find_elements(By.XPATH, 
                    "//img[contains(@src, 'phone') or contains(@src, 'email') or contains(@src, 'location') or contains(@src, 'map')]")
                for icon in icon_elements:
                    try:
                        contact_section = icon.find_element(By.XPATH, "./ancestor::div[contains(@class, 'x1hq5gj4') or contains(@class, 'xx6bls6')][1]")
                        if contact_section:
                            break
                    except:
                        continue
            except Exception as e:
                print(f"Method 2 failed: {e}")
        
        # Method 3: Look for specific contact patterns in the page
        if not contact_section:
            try:
                # Find elements containing email patterns
                email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                all_text_elements = driver.find_elements(By.XPATH, "//*[contains(text(), '@')]")
                
                for element in all_text_elements:
                    if re.search(email_pattern, element.text):
                        try:
                            contact_section = element.find_element(By.XPATH, "./ancestor::div[contains(@class, 'x1hq5gj4') or contains(@class, 'xx6bls6')][1]")
                            if contact_section:
                                break
                        except:
                            continue
            except Exception as e:
                print(f"Method 3 failed: {e}")
        
        if not contact_section:
            print("Contact info section not found, searching entire page...")
            contact_section = driver.find_element(By.TAG_NAME, "body")
        
        # Extract email addresses
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        
        # Look for emails in text content
        try:
            email_elements = contact_section.find_elements(By.XPATH, ".//*[contains(text(), '@')]")
            for element in email_elements:
                text = element.text.strip()
                if text and not any(skip in text.lower() for skip in ['categories', 'page', 'about']):
                    emails_found = email_pattern.findall(text)
                    for email in emails_found:
                        if email not in contact_info['emails']:
                            contact_info['emails'].append(email)
        except Exception as e:
            print(f"Email extraction error: {e}")
        
        # Extract phone numbers
        phone_patterns = [
            r'\+\d{1,3}[\s\-\(\)]?\d{1,4}[\s\-\(\)]?\d{1,4}[\s\-\(\)]?\d{1,9}',  # International format
            r'\d{10,}',  # Simple 10+ digit number
            r'\(\d{3}\)[\s\-]?\d{3}[\s\-]?\d{4}',  # US format
            r'\d{3}[\s\-]\d{3}[\s\-]\d{4}'  # US format without parentheses
        ]
        
        try:
            # Look for phone numbers in spans and divs
            phone_elements = contact_section.find_elements(By.XPATH, 
                ".//*[contains(text(), '+') or contains(text(), '91') or contains(text(), '99') or string-length(translate(text(), '0123456789', '')) < string-length(text()) - 8]")
            
            for element in phone_elements:
                text = element.text.strip()
                if text and len(text) > 5 and not any(skip in text.lower() for skip in ['categories', 'page', 'about', 'sponsored']):
                    # Check if text contains mostly digits and common phone separators
                    clean_text = re.sub(r'[^\d\+\-\(\)\s]', '', text)
                    if len(clean_text) >= 10:  # Minimum phone number length
                        for pattern in phone_patterns:
                            matches = re.findall(pattern, clean_text)
                            for match in matches:
                                # Clean the phone number
                                clean_phone = re.sub(r'[^\d\+]', '', match)
                                if len(clean_phone) >= 10 and clean_phone not in contact_info['phone_numbers']:
                                    contact_info['phone_numbers'].append(match.strip())
        except Exception as e:
            print(f"Phone extraction error: {e}")
        
        # Extract address information
        try:
            address_keywords = ['address', 'location', 'bihar', 'patna', 'india', 'street', 'city', 'state']
            address_elements = contact_section.find_elements(By.XPATH, 
                ".//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'address') or " +
                "contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'bihar') or " +
                "contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'patna') or " +
                "contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'india')]")
            
            for element in address_elements:
                text = element.text.strip()
                if text and len(text) > 10 and not any(skip in text.lower() for skip in ['categories', 'page type', 'about']):
                    # Check if it looks like an address (contains comma or multiple words)
                    if ',' in text or len(text.split()) > 3:
                        contact_info['address'] = text
                        break
        except Exception as e:
            print(f"Address extraction error: {e}")
        
        # Extract website information
        try:
            website_pattern = re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+')
            website_elements = contact_section.find_elements(By.XPATH, 
                ".//*[contains(text(), 'http') or contains(text(), 'www.')]")
            
            for element in website_elements:
                text = element.text.strip()
                websites_found = website_pattern.findall(text)
                for website in websites_found:
                    if 'facebook.com' not in website.lower():
                        contact_info['website'] = website
                        break
                if contact_info['website']:
                    break
        except Exception as e:
            print(f"Website extraction error: {e}")
        
        # Extract map coordinates from background images
        try:
            map_elements = driver.find_elements(By.XPATH, 
                "//div[contains(@style, 'background-image') and contains(@style, 'static_map')]")
            
            for map_element in map_elements:
                style = map_element.get_attribute('style')
                if 'static_map.php' in style:
                    coord_pattern = re.compile(r'center=([0-9.]+)%2C([0-9.]+)')
                    match = coord_pattern.search(style)
                    if match:
                        lat, lng = match.groups()
                        contact_info['map_coordinates'] = {
                            'latitude': float(lat),
                            'longitude': float(lng)
                        }
                        break
        except Exception as e:
            print(f"Map coordinates extraction error: {e}")
        
        # Clean up and validate data
        contact_info['phone_numbers'] = list(set(contact_info['phone_numbers']))
        contact_info['emails'] = list(set(contact_info['emails']))
        
        # Remove obviously wrong phone numbers (like the character-separated one you showed)
        valid_phones = []
        for phone in contact_info['phone_numbers']:
            # Remove phone numbers that have too many non-digit characters or are too long
            digit_count = sum(c.isdigit() for c in phone)
            if digit_count >= 10 and len(phone) < 50:  # Reasonable phone number length
                valid_phones.append(phone)
        
        contact_info['phone_numbers'] = valid_phones
        
        print(f"DEBUG: Found emails: {contact_info['emails']}")
        print(f"DEBUG: Found phones: {contact_info['phone_numbers']}")
        print(f"DEBUG: Found address: {contact_info['address']}")
        
    except Exception as e:
        print(f"Error in main scraping function: {e}")
        import traceback
        traceback.print_exc()
    
    return contact_info

def click_About_Button(driver):
    wait = WebDriverWait(driver, 10)
    print("driver function processing")
    # Method 1: Click by exact href attribute
    try:
        about_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//a[@href='https://www.facebook.com/profile.php?id=100065060851125&sk=about']"
        )))
        about_button.click()
        print("Successfully clicked About button using href")
    
    except (TimeoutException, ElementClickInterceptedException):
        # Method 2: Click by text content
        try:
            about_button = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//a[.//span[text()='About']]"
            )))
            about_button.click()
            print("Successfully clicked About button using text")
        
        except (TimeoutException, ElementClickInterceptedException):
            # Method 3: Click by role and text combination
            try:
                about_button = wait.until(EC.element_to_be_clickable((
                    By.XPATH, "//a[@role='tab' and .//span[text()='About']]"
                )))
                about_button.click()
                print("Successfully clicked About button using role and text")
            
            except (TimeoutException, ElementClickInterceptedException):
                # Method 4: Use JavaScript click as fallback
                about_button = driver.find_element(By.XPATH, "//span[text()='About']/ancestor::a")
                driver.execute_script("arguments[0].click();", about_button)
                print("Successfully clicked About button using JavaScript")

    # Wait a moment to see the result
    time.sleep(2)


data = []

def scrape_facebook_profiles(driver, max_scroll_attempts=9999, is_people=False):
    """
    Enhanced version: Scrapes Facebook profile pages with infinite scrolling capability
    
    Args:
        driver: Selenium WebDriver instance
        max_scroll_attempts: Maximum number of scroll attempts (set to 9999 for near-infinite)
        is_people: Boolean to determine scraping method
    """
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
    
    processed_profiles = set()  
    scroll_attempts = 0
    consecutive_no_new_profiles = 0  # Track consecutive attempts with no new profiles
    total_profiles_found = 0
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    print(f"Starting {'people' if is_people else 'pages'} profile scraping with infinite scroll...")
    
    while scroll_attempts < max_scroll_attempts:
        try:
            print(f"Scroll attempt {scroll_attempts + 1} (Infinite mode: {max_scroll_attempts == 9999})")
            
            # Find all profile links on the current page
            profile_links = driver.find_elements(
                By.CSS_SELECTOR, 
                'a[href*="facebook.com/profile.php"], a[href*="facebook.com/"][class*="x1i10hfl"]'
            )
            
            # Extract and clean profile URLs
            current_profiles = []
            for link in profile_links:
                href = link.get_attribute('href')
                if href and 'profile.php' in href:
                    # Clean the URL to remove extra parameters that might cause duplicates
                    clean_url = href.split('&')[0] if '&' in href else href
                    clean_url = clean_url.split('?')[0] + '?' + clean_url.split('?')[1] if '?' in clean_url else clean_url
                    
                    if clean_url not in processed_profiles:
                        current_profiles.append(clean_url)
            
            # Remove duplicates while preserving order
            current_profiles = list(dict.fromkeys(current_profiles))
            
            print(f"Found {len(current_profiles)} new profiles on this page")
            print(f"Total processed so far: {len(processed_profiles)}")
            
            # If no new profiles found, check if we've reached the end
            if not current_profiles:
                consecutive_no_new_profiles += 1
                print(f"No new profiles found (consecutive attempt {consecutive_no_new_profiles})")
                
                # Scroll down to try to load more content
                print("Scrolling to load more profiles...")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)  # Wait longer for content to load
                
                # Check if page height changed (indicating new content loaded)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    # Page height didn't change, try a few more times
                    if consecutive_no_new_profiles >= 5:
                        print("No new content loaded after multiple attempts. Reached end of results.")
                        break
                else:
                    last_height = new_height
                    consecutive_no_new_profiles = 0  # Reset counter if new content loaded
                
                scroll_attempts += 1
                continue
            
            # Reset the consecutive counter since we found new profiles
            consecutive_no_new_profiles = 0
            total_profiles_found += len(current_profiles)
            
            # Process each profile ONLY ONCE
            for profile_url in current_profiles:
                if profile_url in processed_profiles:
                    print(f"Profile already processed, skipping: {profile_url}")
                    continue
                    
                # Mark as processed BEFORE processing to avoid duplicates
                processed_profiles.add(profile_url)
                
                try:
                    print(f"Processing profile ({len(processed_profiles)}): {profile_url}")
                    
                    # Open profile in new tab
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[-1])
                    driver.get(profile_url)
                    
                    # Wait for page to load
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, "body"))
                    )
                    
                    # Click About button and scrape info
                    click_About_Button(driver)
                    
                    if not is_people:
                        info = scrape_facebook_contact_info(driver, timeout=10)
                    else:
                        info = scrape_contact_and_basic_info(driver) # for people
                                            
                    # Add profile URL to the info for reference
                    info['profile_url'] = profile_url
                    
                    print(f"Profile data: {info}")
                    data.append(info)
                    
                    # Flatten nested info into one dict for CSV
                    flat_info = {
                        'profile_url': info.get('profile_url'),
                        'name': info.get('name') or info.get('profile_name'),
                        'email': ', '.join(info.get('emails', [])) if 'emails' in info else '',
                        'phone': ', '.join(info.get('phone_numbers', [])) if 'phone_numbers' in info else '',
                        'address': info.get('address', ''),
                        'website': info.get('website', ''),
                        'category': ', '.join(info.get('categories', {}).get('categories', [])) if 'categories' in info else '',
                    }

                    # Choose filename based on people or pages
                    filename = 'people_data.csv' if is_people else 'pages_data.csv'
                    fieldnames = ['profile_url', 'name', 'email', 'phone', 'address', 'website', 'category']

                    # Write to CSV
                    append_to_csv(filename, flat_info, fieldnames)

                    
                    # Save data periodically (every 10 profiles) to prevent data loss
                    if len(data) % 10 == 0:
                        print(f"Processed {len(data)} profiles so far...")
                    
                    # Close current tab and return to main search page
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(1)
                    
                except Exception as e:
                    print(f"Error processing profile {profile_url}: {str(e)}")
                    # Make sure we close any extra tabs
                    try:
                        if len(driver.window_handles) > 1:
                            driver.close()
                            driver.switch_to.window(driver.window_handles[0])
                    except:
                        pass
            
            # Scroll down to load more profiles
            print("Scrolling to load more profiles...")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            
            # Update last height
            last_height = driver.execute_script("return document.body.scrollHeight")
            scroll_attempts += 1
            
            # For infinite scrolling, give user feedback every 50 scrolls
            if scroll_attempts % 50 == 0 and max_scroll_attempts == 9999:
                print(f"Infinite scroll progress: {scroll_attempts} scrolls completed, {len(processed_profiles)} profiles processed")
                
        except Exception as e:
            print(f"Error in main loop: {str(e)}")
            scroll_attempts += 1
            time.sleep(2)
            
            # Try to recover by scrolling
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
            except:
                pass
    
    print(f"Finished processing. Total profiles processed: {len(processed_profiles)}")
    print(f"Total data entries collected: {len(data)}")
    print(f"Total scroll attempts made: {scroll_attempts}")
    
    return list(processed_profiles)


def click_peoples_button(driver):
    wait = WebDriverWait(driver, 10)
    current_url = driver.current_url
    
    print(f"Current URL before clicking: {current_url}")
    
    # Strategy 3: Look for Pages link by href
    try:
        print("Strategy 3: Looking for Pages by href attribute...")
        
        pages_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'people') and .//span[text()='People']]"))
        )
        print(f"Found People link: {pages_link.get_attribute('href')}")
        
        # Scroll to element
        driver.execute_script("arguments[0].scrollIntoView(true);", pages_link)
        time.sleep(1)
        
        pages_link.click()
        
        # Verify navigation
        time.sleep(3)
        new_url = driver.current_url
        print(f"New URL after click: {new_url}")
        
        if new_url != current_url or "pages" in new_url.lower():
            print("Successfully navigated to People!")
            return True
        else:
            print("URL didn't change, click may not have worked")
            
    except (TimeoutException, ElementClickInterceptedException) as e:
        print(f"Strategy 3 failed: {str(e)}")
        print(f"Direct navigation failed: {str(e)}")
   
    return False
    

def click_pages_button(driver):
    """
    Function to click the Pages button on Facebook with proper verification
    """
    wait = WebDriverWait(driver, 10)
    current_url = driver.current_url
    
    print(f"Current URL before clicking: {current_url}")
    
    # Strategy 3: Look for Pages link by href
    try:
        print("Strategy 3: Looking for Pages by href attribute...")
        
        pages_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'pages') and .//span[text()='Pages']]"))
        )
        print(f"Found Pages link: {pages_link.get_attribute('href')}")
        
        # Scroll to element
        driver.execute_script("arguments[0].scrollIntoView(true);", pages_link)
        time.sleep(1)
        
        pages_link.click()
        
        # Verify navigation
        time.sleep(3)
        new_url = driver.current_url
        print(f"New URL after click: {new_url}")
        
        if new_url != current_url or "pages" in new_url.lower():
            print("Successfully navigated to Pages!")
            return True
        else:
            print("URL didn't change, click may not have worked")
            
    except (TimeoutException, ElementClickInterceptedException) as e:
        print(f"Strategy 3 failed: {str(e)}")
        print(f"Direct navigation failed: {str(e)}")
   
    return False

def click_people_button(driver):
    wait = WebDriverWait(driver, 10)
    current_url = driver.current_url
    
    print(f"Current URL before clicking: {current_url}")
    
    # Strategy 3: Look for People link by href
    try:
        print("Strategy 3: Looking for People by href attribute...")
        
        people_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'people') and .//span[text()='People']]"))
        )
        
        print(f"Found People link: {people_link.get_attribute('href')}")
        
        # Scroll to element
        driver.execute_script("arguments[0].scrollIntoView(true);", people_link)
        time.sleep(1)
        
        people_link.click()
        
        # Verify navigation
        time.sleep(3)
        new_url = driver.current_url
        print(f"New URL after click: {new_url}")
        
        if new_url != current_url or "people" in new_url.lower():
            print("Successfully navigated to People!")
            return True
        else:
            print("URL didn't change, click may not have worked")
            
    except (TimeoutException, ElementClickInterceptedException) as e:
        print(f"Strategy 3 failed: {str(e)}")
        print(f"Direct navigation failed: {str(e)}")
   
    return False

def facebook_search(driver, search_term):
    """Function to perform search on Facebook"""
    try:
        print(f"Searching for: {search_term}")
        
        # Wait for the search input to be present
        wait = WebDriverWait(driver, 10)
        
        # Find the search input field - it's nested inside a label
        # Using multiple strategies to find the search box
        time.sleep(3)
        search_input = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
        search_input.click()
        
        # Clear any existing text and enter the search term
        search_input.clear()
        search_input.send_keys(search_term)
        
        # Press Enter to search
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)
        
        print("Search completed!")
        
    except Exception as e:
        print(f"Error during search: {str(e)}")

def facebook_login(email, password):
    # Set up Chrome options
    chrome_options = Options()
    # Uncomment the next line to run in headless mode
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_argument("--disable-images")  # Optional: speeds up loading
    chrome_options.add_argument("--disable-javascript-harmony-shipping")
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-backgrounding-occluded-windows")
    chrome_options.add_argument("--disable-translate")
    chrome_options.add_argument("--disable-ipc-flooding-protection")
    
    # Initialize the driver
    # Note: You'll need to have ChromeDriver installed and in your PATH
    # Or specify the path to ChromeDriver using Service
    driver = webdriver.Chrome(options=chrome_options)
    
    
    try:
        # Navigate to Facebook
        print("Navigating to Facebook...")
        driver.get("https://www.facebook.com/")
        
        
        # Wait for the page to load and find the email field
        wait = WebDriverWait(driver, 10)
        
        # Find email field using multiple strategies for reliability
        email_field = wait.until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        
        print("Email field found, entering email...")
        email_field.clear()
        email_field.send_keys(email)
        
        # Find password field
        password_field = driver.find_element(By.ID, "pass")
        
        print("Password field found, entering password...")
        password_field.clear()
        password_field.send_keys(password)
        
        print("Credentials entered successfully!")
        
        # Optional: Find and click login button
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()
        
        # Wait a bit to see the result
        time.sleep(3)
        if detect_identity_verification_screen(driver) or detect_recaptcha_verification_screen(driver):
            print("acc blocked")
            return True
        search_term = "political campaign"
        facebook_search(driver, search_term)
        time.sleep(3)
        
        
        # Reset data list for each section
        global data
        data = []
        
        print("=== SCRAPING PEOPLE ===")
        data = []  
        click_people_button(driver)
        time.sleep(1.5)
        scrape_facebook_profiles(driver,is_people=True)
        people_data = data.copy()  # Save people data
        
        print("=== SCRAPING PAGES ===")
        click_pages_button(driver)
        time.sleep(1.5)
        scrape_facebook_profiles(driver,is_people=False)
        pages_data = data.copy()  # Save pages data
        
        print(f"\n=== FINAL RESULTS ===")
        print(f"Pages scraped: {len(pages_data)}")
        print(f"People scraped: {len(people_data)}")
        print(f"Total profiles scraped: {len(pages_data) + len(people_data)}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        # Close the browser
        print("Closing browser...")
        driver.quit()

# Example usage
if __name__ == "__main__":
    # Replace with actual credentials for testing
    # WARNING: Never hardcode real credentials in production code
    email = ""
    password = ""
    
    # Call the function
    
    facebook_login(email, password)